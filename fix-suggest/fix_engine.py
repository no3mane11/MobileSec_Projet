from rules import FIX_RULES

def generate_fixes(report):
    fixes = []
    # On descend dans la structure créée par ReportGen
    audit = report.get("detailed_analysis", {})

    for rule in FIX_RULES:
        try:
            # On vérifie si la condition de la règle est remplie
            if rule["condition"](audit):
                fixes.append({
                    "issue": rule["issue"],
                    "severity": rule["severity"],
                    "recommendation": rule["recommendation"],
                    "example_fix": rule["example_fix"]
                })
        except Exception as e:
            continue

    return {
        "status": "Success",
        "total_recommendations": len(fixes),
        "recommendations": fixes
    }