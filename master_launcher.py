import subprocess
import os
import time

# Configuration des chemins et des ports
# Modifie les noms des dossiers si nécessaire pour correspondre à ton architecture
SERVICES = [
    {"name": "APK-Scanner", "path": "apk-scanner", "port": 8001},
    {"name": "Secret-Hunter", "path": "secret-hunter", "port": 8002},
    {"name": "Crypto-Check", "path": "crypto-check", "port": 8003},
    {"name": "Network-Inspector", "path": "network-inspector", "port": 8004},
    {"name": "Report-Gen", "path": "report-gen", "port": 8005},
    {"name": "Fix-Suggest", "path": "fix-suggest", "port": 8006},
    {"name": "CI-Connector", "path": "ci-connector", "port": 8007},
]

def launch_services():
    print("--- Démarrage de la suite MobileSec-MS ---")
    
    for service in SERVICES:
        path = service["path"]
        port = service["port"]
        name = service["name"]
        
        # Commande pour Windows (ouvre un nouveau terminal cmd)
        # On utilise 'start' pour créer une nouvelle fenêtre par service
        cmd = f'start "{name}" cmd /k "cd {path} && python -m uvicorn main:app --reload --port {port}"'
        
        print(f"Lancement de {name} sur le port {port}...")
        subprocess.Popen(cmd, shell=True)
        time.sleep(1)  # Petite pause pour éviter les conflits de démarrage

    print("\n--- Tous les services ont été lancés avec succès ---")
    print("Accédez au ReportGen sur : http://127.0.0.1:8005/docs")

if __name__ == "__main__":
    launch_services()