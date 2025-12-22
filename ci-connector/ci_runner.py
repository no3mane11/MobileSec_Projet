import requests
import json
import os

SERVICES = {
    "scanners": {
        "apk_scanner": "http://localhost:8001/scan",
        "secret_hunter": "http://localhost:8002/scan",
        "crypto_check": "http://localhost:8003/scan",
        "network_inspector": "http://localhost:8004/scan"
    },
    "report_gen": "http://localhost:8005/generate-report", 
    "fix_suggest": "http://localhost:8006/suggest-fixes"
}

def run_ci_scan(uploaded_file):
    raw_results = {}
    
    # ÉTAPE 1 : Lire le contenu du fichier envoyé par React
    apk_content = uploaded_file.file.read()

    # ÉTAPE 2 : Envoi aux 4 scanners
    for name, url in SERVICES["scanners"].items():
        try:
            # On recrée l'envoi multipart pour chaque microservice
            files = {"file": (uploaded_file.filename, apk_content)}
            response = requests.post(url, files=files, timeout=30)
            raw_results[name] = response.json()
        except Exception as e:
            raw_results[name] = {"error": str(e), "count": 0}

    # ÉTAPE 3 : Rapport Global
    try:
        report_response = requests.post(SERVICES["report_gen"], json=raw_results)
        final_report = report_response.json()
    except Exception as e:
        final_report = {"error": "ReportGen failed"}

    # ÉTAPE 4 : Fix Suggest
    try:
        fix_response = requests.post(SERVICES["fix_suggest"], json=final_report)
        remediations = fix_response.json()
    except Exception as e:
        remediations = {"error": "FixSuggest failed"}

    return {
        "ci_status": "SUCCESS",
        "package_analyzed": final_report.get("report_info", {}).get("app_package"),
        "security_score": final_report.get("security_summary", {}).get("overall_score"),
        "vulnerabilities_count": final_report.get("security_summary", {}).get("vulnerabilities_found"),
        "full_report": final_report,
        "solutions": remediations
    }