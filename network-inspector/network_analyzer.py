import os
import re
import tempfile
from androguard.core.apk import APK

def analyze_network(uploaded_file):
    temp_dir = tempfile.gettempdir()
    apk_path = os.path.join(temp_dir, "network_scan.apk")

    issues = []

    try:
        # 1. Sauvegarde APK
        with open(apk_path, "wb") as f:
            f.write(uploaded_file.file.read())

        apk = APK(apk_path)

        # 2. Analyse AndroidManifest.xml
        manifest = apk.get_android_manifest_xml()
        app_node = manifest.find("application")

        cleartext = app_node.get(
            "{http://schemas.android.com/apk/res/android}usesCleartextTraffic"
        )

        if cleartext == "true":
            issues.append({
                "issue": "Cleartext traffic allowed",
                "severity": "CRITIQUE",
                "location": "AndroidManifest.xml"
            })

        # 3. Recherche d'URLs HTTP en clair
        for file_name in apk.get_files():
            if file_name.endswith((".xml", ".txt", ".dex")):
                try:
                    content = apk.get_file(file_name).decode("utf-8", errors="ignore")
                    if re.search(r"http://", content):
                        issues.append({
                            "issue": "HTTP URL detected",
                            "severity": "ÉLEVÉ",
                            "location": file_name
                        })
                except:
                    continue

        return {
            "network_issues": issues,
            "count": len(issues)
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        if os.path.exists(apk_path):
            os.remove(apk_path)
