import os
import re
import tempfile
from androguard.core.apk import APK

# Règles basées sur les standards OWASP Mobile
CRYPTO_PATTERNS = {
    "Weak Hash Algorithm": r"MD5|SHA1",
    "Insecure AES Mode": r"AES/ECB",
    "Hardcoded Crypto Algorithm": r"Cipher\.getInstance\(\"[A-Za-z0-9/]+\"\)",
}

def analyze_crypto(uploaded_file):
    temp_dir = tempfile.gettempdir()
    apk_path = os.path.join(temp_dir, "crypto_scan.apk")

    try:
        # 1. Sauvegarde de l'APK reçu via l'API
        with open(apk_path, "wb") as f:
            f.write(uploaded_file.file.read())

        apk = APK(apk_path)
        issues = []

        # 2. Analyse des fichiers de l'APK
        for file_name in apk.get_files():
            # IMPORTANT : Scanner les fichiers .dex pour trouver le code compilé
            if file_name.endswith((".xml", ".txt", ".dex")):
                try:
                    raw_data = apk.get_file(file_name)
                    # Décodage avec "ignore" pour extraire les chaînes de caractères du binaire
                    content = raw_data.decode("utf-8", errors="ignore")
                    
                    for issue_type, pattern in CRYPTO_PATTERNS.items():
                        if re.search(pattern, content):
                            issues.append({
                                "type": issue_type,
                                "detail": f"Detected: {pattern}",
                                "location": file_name
                            })
                except:
                    continue

        # Suppression des doublons potentiels si le même motif apparaît plusieurs fois
        unique_issues = [dict(t) for t in {tuple(d.items()) for d in issues}]

        return {
            "crypto_issues": unique_issues,
            "count": len(unique_issues)
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        # Nettoyage du fichier temporaire après analyse
        if os.path.exists(apk_path):
            os.remove(apk_path)