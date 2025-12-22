def build_report(data: dict):
    # Extraction avec valeurs par défaut pour éviter les erreurs NoneType
    apk = data.get("apk_scanner", {})
    secrets = data.get("secret_hunter", {})
    crypto = data.get("crypto_check", {})
    network = data.get("network_inspector", {})

    # Calcul précis des vulnérabilités
    total_issues = (
        len(apk.get("dangerous_permissions", [])) +
        secrets.get("count", 0) +
        crypto.get("count", 0) +
        network.get("count", 0)
    )

    if apk.get("debuggable") is True:
        total_issues += 1

    # Évaluation du niveau
    if total_issues == 0:
        level = "SÉCURISÉ (HIGH)"
    elif 1 <= total_issues <= 5:
        level = "VIGILANCE (MEDIUM)"
    else:
        level = "CRITIQUE (LOW)"

    return {
        "report_info": {
            "status": "Finalized",
            "app_package": apk.get("package", "com.unknown.app"),
            "scan_engine_version": "2.0"
        },
        "security_summary": {
            "overall_score": level,
            "vulnerabilities_found": total_issues,
            "risk_assessment": generate_summary(level, total_issues)
        },
        "detailed_analysis": {
            "static_manifest": {
                "permissions": apk.get("dangerous_permissions", []),
                "is_debuggable": apk.get("debuggable", False),
                "allow_backup": apk.get("allow_backup", False)
            },
            "sensitive_data": {
                "secrets": secrets.get("secrets_found", []),
                "count": secrets.get("count", 0)
            },
            "cryptography": {
                "issues": crypto.get("crypto_issues", []),
                "count": crypto.get("count", 0)
            },
            "network_security": {
                "issues": network.get("network_issues", []),
                "count": network.get("count", 0)
            }
        }
    }

def generate_summary(level, count):
    if "HIGH" in level:
        return "Aucune faille majeure détectée."
    if "MEDIUM" in level:
        return f"Attention : {count} vulnérabilités détectées."
    return f"ALERTE : {count} failles critiques trouvées. Action requise."