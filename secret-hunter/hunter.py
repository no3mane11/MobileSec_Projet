import os
import re
import tempfile
from androguard.core.apk import APK

# Regex optimisées
SECRET_PATTERNS = {
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Firebase URL": r"https://[a-z0-9\-]+\.firebaseio\.com",
    "Stripe Key": r"sk_test_[0-9a-zA-Z]{24}",
    "Generic Secret": r"(?i)(api_key|secret|password|token)[\s:=]+['\"][A-Za-z0-9\-_]{16,}['\"]"
}

def hunt_secrets(uploaded_file):
    temp_dir = tempfile.gettempdir()
    apk_path = os.path.join(temp_dir, "secret_scan.apk")

    try:
        # 1. Sauvegarde l'APK proprement
        with open(apk_path, "wb") as f:
            content = uploaded_file.file.read()
            f.write(content)

        apk = APK(apk_path)
        results = []

        # 2. ANALYSE DES RESSOURCES (strings.xml binaire)
        resources = apk.get_android_resources()
        if resources:
            # On récupère toutes les strings de l'APK (déchiffrées par Androguard)
            all_strings = resources.get_strings_resources()
            for string_value in all_strings:
                # FORCE LA CONVERSION EN STRING pour éviter l'erreur "expected string or bytes"
                val_str = str(string_value) 
                for name, pattern in SECRET_PATTERNS.items():
                    if re.search(pattern, val_str):
                        results.append({
                            "type": name,
                            "value": val_str,
                            "location": "resources.arsc"
                        })

        # 3. ANALYSE DES FICHIERS DEX (Le code source compilé)
        for file_name in apk.get_files():
            if file_name.endswith(".dex"):
                try:
                    raw_data = apk.get_file(file_name)
                    # On décode en ignorant les erreurs pour lire le texte au milieu du binaire
                    content_str = raw_data.decode("utf-8", errors="ignore")
                    
                    for name, pattern in SECRET_PATTERNS.items():
                        matches = re.findall(pattern, content_str)
                        for m in matches:
                            # On évite les doublons
                            if not any(r['value'] == m for r in results):
                                results.append({
                                    "type": name,
                                    "value": m,
                                    "location": file_name
                                })
                except:
                    continue

        return {
            "secrets_found": results,
            "count": len(results)
        }

    except Exception as e:
        return {"error": f"Erreur critique : {str(e)}"}

    finally:
        if os.path.exists(apk_path):
            os.remove(apk_path)