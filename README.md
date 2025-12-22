<h1 style="color:#2E86C1;">MobileSec-MS</h1>

MobileSec-MS est une plateforme basée sur une architecture microservices dédiée à l’analyse automatisée de la sécurité des applications mobiles Android (fichiers APK).

Elle permet de détecter des vulnérabilités courantes, de générer des rapports détaillés et de proposer des recommandations de correction exploitables.  
Le projet s’inscrit dans une démarche DevSecOps et s’appuie sur les bonnes pratiques définies par l’OWASP Mobile Security Testing Guide.

<hr/>

<h2 style="color:#117864;">Sommaire</h2>

- Présentation générale  
- Objectifs du projet  
- Architecture globale  
- Description des microservices  
- Prérequis techniques  
- Installation  
- Utilisation  
- Documentation des API  
- Tests  
- Intégration CI/CD  
- Structure du projet  
- Développement et contribution  
- Licence  

<hr/>

<h2 style="color:#117864;">Présentation générale</h2>

MobileSec-MS permet d’analyser automatiquement plusieurs aspects de la sécurité des applications mobiles Android, notamment :

- Les permissions et la configuration du fichier AndroidManifest  
- La présence de secrets exposés (clés API, tokens, URLs sensibles)  
- Les implémentations cryptographiques faibles  
- Les configurations réseau non sécurisées  
- Les mauvaises pratiques de développement  

L’objectif est de fournir une analyse rapide, reproductible et facilement intégrable dans des pipelines d’intégration continue.

<hr/>

<h2 style="color:#117864;">Objectifs du projet</h2>

Les principaux objectifs de MobileSec-MS sont :

- Automatiser l’analyse de sécurité des applications mobiles Android  
- Décomposer l’analyse en microservices indépendants et modulaires  
- Générer des rapports clairs et exploitables  
- Proposer des recommandations de correction alignées avec OWASP MASVS  
- Faciliter l’intégration dans des pipelines CI/CD  

<hr/>

<h2 style="color:#117864;">Architecture globale</h2>

La plateforme repose sur une architecture microservices.  
Chaque service est responsable d’un type précis d’analyse de sécurité.

<b>Flux général de fonctionnement :</b>

APK uploadé → Analyses par plusieurs services → Agrégation des résultats → Génération du rapport → Suggestions de corrections

Les services communiquent via des API REST et peuvent être déployés ou testés indépendamment.  
Un script central nommé <b>master_launcher.py</b> permet de lancer l’ensemble des services en local pour le développement.

<hr/>

<h2 style="color:#117864;">Description des microservices</h2>

<h3 style="color:#1F618D;">APK-Scanner (port 8001)</h3>

<b>Rôle :</b>  
Analyse statique de la structure de l’APK et du fichier AndroidManifest.xml.

<b>Fonctionnalités :</b>  
- Extraction des informations générales de l’application  
- Analyse des permissions dangereuses  
- Vérification des flags debuggable et allowBackup  
- Détection des composants exportés  

<b>Technologies :</b>  
FastAPI, Uvicorn, Androguard, python-multipart

---

<h3 style="color:#1F618D;">Secret-Hunter (port 8002)</h3>

<b>Rôle :</b>  
Détection des secrets et informations sensibles codées en dur.

<b>Fonctionnalités :</b>  
- Analyse des ressources et fichiers DEX  
- Détection de clés Google API, Firebase, Stripe et OAuth  
- Identification de l’emplacement et du type de secret  

<b>Technologies :</b>  
FastAPI, Uvicorn, Androguard, python-multipart

---

<h3 style="color:#1F618D;">Crypto-Check (port 8003)</h3>

<b>Rôle :</b>  
Analyse des mécanismes cryptographiques utilisés dans l’application.

<b>Fonctionnalités :</b>  
- Détection des algorithmes faibles comme MD5 et SHA1  
- Identification des modes AES non sécurisés (ECB)  
- Analyse des implémentations cryptographiques dans les fichiers DEX  

<b>Technologies :</b>  
FastAPI, Uvicorn, Androguard

---

<h3 style="color:#1F618D;">Network-Inspector (port 8004)</h3>

<b>Rôle :</b>  
Analyse des configurations réseau et de la sécurité des communications.

<b>Fonctionnalités :</b>  
- Détection du trafic en clair (HTTP)  
- Analyse des paramètres networkSecurityConfig  
- Identification des URLs non sécurisées  

<b>Technologies :</b>  
FastAPI, Uvicorn, Androguard

---

<h3 style="color:#1F618D;">Report-Gen (port 8005)</h3>

<b>Rôle :</b>  
Centralisation et agrégation des résultats d’analyse.

<b>Fonctionnalités :</b>  
- Regroupement des résultats de tous les analyseurs  
- Calcul d’un niveau de risque global  
- Génération de rapports structurés au format JSON  

<b>Technologies :</b>  
FastAPI, Uvicorn

---

<h3 style="color:#1F618D;">Fix-Suggest (port 8006)</h3>

<b>Rôle :</b>  
Proposition de recommandations de correction.

<b>Fonctionnalités :</b>  
- Association des vulnérabilités aux exigences OWASP MASVS  
- Suggestions de corrections concrètes  
- Exemples de modifications du fichier AndroidManifest  

<b>Technologies :</b>  
FastAPI, Uvicorn

---

<h3 style="color:#1F618D;">CI-Connector (port 8007)</h3>

<b>Rôle :</b>  
Orchestration des analyses dans un contexte CI/CD.

<b>Fonctionnalités :</b>  
- Lancement automatisé de l’ensemble des analyses  
- Intégration avec GitHub Actions et GitLab CI  
- Retour d’un résultat global incluant rapports et recommandations  

<b>Technologies :</b>  
FastAPI, Uvicorn, Requests

<hr/>

<h2 style="color:#117864;">Prérequis techniques</h2>

- Python version 3.10 ou supérieure  
- Java JDK 11 ou 17 (nécessaire pour l’analyse des APK)  
- Git  
- Postman ou curl (optionnel pour les tests)

<hr/>

<h2 style="color:#117864;">Installation</h2>

Cloner le dépôt :

```bash
git clone https://github.com/no3mane11/MobileSec_Projet.git
cd MobileSec_Projet
