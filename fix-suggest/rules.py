FIX_RULES = [
    # --- ANALYSE DU MANIFESTE ---
    {
        "condition": lambda r: r.get("static_manifest", {}).get("is_debuggable") is True,
        "issue": "Application en mode debuggable",
        "severity": "CRITIQUE",
        "recommendation": "Désactiver le mode debuggable dans le fichier AndroidManifest.xml.",
        "example_fix": "android:debuggable=\"false\""
    },
    {
        "condition": lambda r: r.get("static_manifest", {}).get("allow_backup") is True,
        "issue": "Sauvegarde des données (Backup) autorisée",
        "severity": "MOYEN",
        "recommendation": "Désactiver allowBackup pour empêcher l'extraction des données via ADB.",
        "example_fix": "android:allowBackup=\"false\""
    },
    {
        "condition": lambda r: len(r.get("static_manifest", {}).get("permissions", [])) > 0,
        "issue": "Permissions dangereuses détectées",
        "severity": "ÉLEVÉ",
        "recommendation": "Supprimer les permissions non essentielles (SMS, Stockage) dans le Manifeste.",
        "example_fix": "Retirer les balises <uses-permission> inutiles."
    },

    # --- EXPOSITION DE SECRETS (Clé: sensitive_data) ---
    {
        "condition": lambda r: r.get("sensitive_data", {}).get("count", 0) > 0,
        "issue": "Secrets ou Clés d'API exposés",
        "severity": "CRITIQUE",
        "recommendation": "Ne stockez jamais de clés en clair. Utilisez un Secret Manager.",
        "example_fix": "Déplacer la clé vers un environnement sécurisé."
    },

    # --- CRYPTOGRAPHIE (Clé: cryptography) ---
    {
        "condition": lambda r: r.get("cryptography", {}).get("count", 0) > 0,
        "issue": "Cryptographie obsolète ou non sécurisée",
        "severity": "CRITIQUE",
        "recommendation": "Remplacer MD5/SHA-1 par SHA-256 et utiliser AES/GCM.",
        "example_fix": "Cipher.getInstance(\"AES/GCM/NoPadding\")"
    },

    # --- RÉSEAU (Clé: network_security) ---
    {
        "condition": lambda r: r.get("network_security", {}).get("count", 0) > 0,
        "issue": "Trafic réseau non chiffré (HTTP)",
        "severity": "CRITIQUE",
        "recommendation": "Forcez l'utilisation du HTTPS pour toutes les communications.",
        "example_fix": "android:usesCleartextTraffic=\"false\""
    }
]