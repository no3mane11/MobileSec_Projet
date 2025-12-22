MobileSec-MS

MobileSec-MS est une plateforme basée sur une architecture microservices dédiée à l’analyse automatisée de la sécurité des applications mobiles Android.
Elle permet de détecter des vulnérabilités courantes dans les fichiers APK, de générer des rapports détaillés et de proposer des recommandations de correction exploitables.

Ce projet s’inscrit dans une démarche DevSecOps et s’appuie sur les bonnes pratiques définies par l’OWASP Mobile Security Testing Guide.

Sommaire

Présentation générale

Objectifs du projet

Architecture globale

Description des microservices

Prérequis techniques

Installation

Utilisation

Documentation des API

Tests

Intégration CI/CD

Structure du projet

Développement et contribution

Licence

1. Présentation générale

MobileSec-MS permet d’analyser automatiquement plusieurs aspects de sécurité des applications mobiles, notamment :

Les permissions Android et la configuration du manifeste

La présence de secrets exposés (clés API, tokens, URLs sensibles)

Les implémentations cryptographiques faibles

Les configurations réseau non sécurisées

Les mauvaises pratiques de développement

L’objectif principal est de fournir une analyse rapide, reproductible et intégrable dans des pipelines d’intégration continue.

2. Objectifs du projet

Les objectifs principaux de MobileSec-MS sont :

Automatiser l’analyse de sécurité des applications mobiles Android

Décomposer l’analyse en microservices indépendants et modulaires

Générer des rapports clairs et exploitables

Proposer des recommandations de correction alignées avec OWASP MASVS

Faciliter l’intégration dans des pipelines CI/CD

3. Architecture globale

La plateforme repose sur une architecture microservices.
Chaque service est responsable d’un type précis d’analyse.

Flux général :

APK uploadé → Analyse par plusieurs services → Agrégation des résultats → Génération du rapport → Suggestions de corrections

Les services communiquent via des API REST et peuvent être déployés ou testés indépendamment.

Un script central (master_launcher.py) permet de lancer l’ensemble des services en local pour le développement.

4. Description des microservices
4.1 APK-Scanner (port 8001)

Rôle
Analyse statique de la structure de l’APK et du fichier AndroidManifest.xml.

Fonctionnalités principales

Extraction des informations générales de l’application

Analyse des permissions dangereuses

Vérification des flags debuggable et allowBackup

Détection des composants exportés

Technologies
FastAPI, Uvicorn, Androguard, python-multipart

4.2 Secret-Hunter (port 8002)

Rôle
Détection des secrets et informations sensibles codées en dur.

Fonctionnalités principales

Analyse des ressources et fichiers DEX

Détection de clés Google API, Firebase, Stripe, OAuth

Identification de l’emplacement et du type de secret

Technologies
FastAPI, Uvicorn, Androguard, python-multipart

4.3 Crypto-Check (port 8003)

Rôle
Analyse des mécanismes cryptographiques utilisés dans l’application.

Fonctionnalités principales

Détection des algorithmes faibles (MD5, SHA1)

Identification des modes AES non sécurisés (ECB)

Analyse des implémentations cryptographiques dans les DEX

Technologies
FastAPI, Uvicorn, Androguard

4.4 Network-Inspector (port 8004)

Rôle
Analyse des configurations réseau et de la sécurité des communications.

Fonctionnalités principales

Détection du trafic en clair (HTTP)

Analyse des paramètres networkSecurityConfig

Identification des URLs non sécurisées

Technologies
FastAPI, Uvicorn, Androguard

4.5 Report-Gen (port 8005)

Rôle
Agrégation des résultats des différents analyseurs.

Fonctionnalités principales

Centralisation des données d’analyse

Calcul d’un niveau de risque global

Génération de rapports structurés en JSON

Technologies
FastAPI, Uvicorn

4.6 Fix-Suggest (port 8006)

Rôle
Proposition de recommandations de correction.

Fonctionnalités principales

Association des vulnérabilités aux exigences OWASP MASVS

Suggestions de corrections concrètes

Exemples de modifications AndroidManifest

Technologies
FastAPI, Uvicorn

4.7 CI-Connector (port 8007)

Rôle
Orchestration des analyses dans un contexte CI/CD.

Fonctionnalités principales

Lancement automatisé de l’ensemble des analyses

Intégration avec GitHub Actions et GitLab CI

Retour d’un résultat global incluant rapports et recommandations

Technologies
FastAPI, Uvicorn, Requests

5. Prérequis techniques

Python version 3.10 ou supérieure

Java JDK 11 ou 17 (nécessaire pour l’analyse des APK)

Git

Postman ou curl (optionnel pour les tests)

6. Installation

Cloner le dépôt :

git clone https://github.com/no3mane11/MobileSec_Projet.git
cd MobileSec_Projet


Installer les dépendances principales :

pip install fastapi uvicorn androguard python-multipart requests


Chaque microservice peut également disposer de son propre fichier requirements.txt.

7. Utilisation

Lancement de tous les services en local :

python master_launcher.py


Accès aux interfaces Swagger :

http://127.0.0.1:8001/docs

…

http://127.0.0.1:8007/docs

Les APK peuvent être envoyés via Swagger UI ou via des requêtes API.

8. Documentation des API

Chaque microservice expose automatiquement sa documentation grâce à FastAPI.

Exemples d’endpoints principaux :

POST /scan pour les services d’analyse

POST /generate-report pour la génération du rapport

POST /suggest-fixes pour les recommandations

POST /run-ci-scan pour une analyse complète automatisée

9. Tests

Des APK de test sont fournis pour valider le fonctionnement des services.
Les tests peuvent être réalisés manuellement via Swagger ou automatiquement via le CI-Connector.

10. Intégration CI/CD

Le projet peut être intégré dans des pipelines CI/CD tels que GitHub Actions ou GitLab CI afin d’automatiser les analyses de sécurité à chaque push ou pull request.

11. Structure du projet
MobileSec-MS/
├── apk-scanner/
├── secret-hunter/
├── crypto-check/
├── network-inspector/
├── report-gen/
├── fix-suggest/
├── ci-connector/
├── master_launcher.py
├── samples/
└── docs/

12. Développement et contribution

Les contributions sont possibles via des branches dédiées.
Les ajouts recommandés incluent :

Support des applications iOS (IPA)

Nouveaux analyseurs de vulnérabilités

Tableau de bord web

Conteneurisation Docker

13. Licence

Ce projet est distribué sous licence MIT.
Il est destiné à un usage académique et pédagogique.

Note finale
Ce projet est réalisé dans un cadre universitaire afin de démontrer l’utilisation d’une architecture microservices pour l’analyse de sécurité mobile.
Une utilisation en production nécessiterait des mécanismes supplémentaires de sécurité, d’authentification et de montée en charge.
