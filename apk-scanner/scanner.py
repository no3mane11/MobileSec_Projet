import os
import tempfile
from androguard.core.apk import APK

def analyze_apk(uploaded_file):
    temp_dir = tempfile.gettempdir()
    apk_path = os.path.join(temp_dir, "to_analyze.apk")

    try:
        # 1. Sauvegarde temporaire de l'APK
        with open(apk_path, "wb") as f:
            f.write(uploaded_file.file.read())

        # 2. Chargement de l'APK
        apk = APK(apk_path)

        # 3. Permissions
        permissions = apk.get_permissions()
        dangerous = [
            p for p in permissions
            if any(key in p for key in ["READ", "WRITE", "CAMERA", "SMS"])
        ]

        # 4. Lecture du AndroidManifest.xml
        manifest = apk.get_android_manifest_xml()
        app_node = manifest.find("application")

        debuggable = app_node.get(
            "{http://schemas.android.com/apk/res/android}debuggable"
        ) == "true"

        allow_backup = app_node.get(
            "{http://schemas.android.com/apk/res/android}allowBackup"
        ) == "true"

        # 5. Résultat final
        return {
            "package": apk.get_package(),
            "dangerous_permissions": dangerous,
            "debuggable": debuggable,
            "allow_backup": allow_backup,
            "exported_activities": apk.get_activities()
        }

    except Exception as e:
        return {"error": f"Erreur lors de l'analyse : {str(e)}"}

    finally:
        # 6. Nettoyage
        if os.path.exists(apk_path):
            os.remove(apk_path)
