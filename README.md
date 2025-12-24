<h1 style="color:#2E86C1;">MobileSec-MS — Plateforme d’analyse de sécurité mobile</h1>

MobileSec-MS est une plateforme basée sur une architecture microservices dédiée à l’analyse automatisée de la sécurité des applications mobiles Android (fichiers APK).

Elle permet de détecter des vulnérabilités courantes, de générer des rapports détaillés et de proposer des recommandations de correction exploitables.  
Le projet s’inscrit dans une démarche DevSecOps et s’appuie sur les bonnes pratiques définies par l’OWASP Mobile Security Testing Guide.

<hr/>

<h2 style="color:#117864;">Présentation générale</h2>

MobileSec-MS analyse automatiquement plusieurs aspects critiques de la sécurité des applications mobiles Android, notamment les permissions, la configuration du manifeste, la présence de secrets exposés, les mécanismes cryptographiques utilisés et les paramètres de sécurité réseau.

L’objectif est de fournir une analyse fiable, reproductible et facilement intégrable dans des pipelines d’intégration continue, tout en restant compréhensible pour les développeurs et les équipes sécurité.

<hr/>

<h2 style="color:#117864;">Objectifs du projet</h2>

Les objectifs principaux de MobileSec-MS sont :
<ul>
<li>Automatiser l’analyse de sécurité des applications mobiles Android</li>
<li>Décomposer l’analyse en microservices indépendants et modulaires</li>
<li>Générer des rapports clairs et exploitables</li>
<li>Proposer des recommandations de correction alignées avec OWASP MASVS</li>
<li>Faciliter l’intégration dans des pipelines CI/CD</li>
</ul>

<hr/>

<h2 style="color:#117864;">Architecture globale</h2>

La plateforme repose sur une architecture microservices dans laquelle chaque service est responsable d’un type précis d’analyse de sécurité.

<b>Flux général de fonctionnement :</b><br/>
APK uploadé → Analyses par plusieurs services → Agrégation des résultats → Génération du rapport → Suggestions de corrections

Les services communiquent via des API REST et peuvent être déployés ou testés indépendamment.  
Un script central nommé <b>master_launcher.py</b> permet de lancer l’ensemble des services en local pour le développement et les démonstrations.

<hr/>

<h2 style="color:#117864;">Microservices</h2>

<h3 style="color:#1F618D;">APK-Scanner (port 8001)</h3>
<b>Rôle :</b> Analyse statique de la structure de l’APK et du fichier AndroidManifest.xml.<br/>
<b>Fonctionnalités :</b> Analyse des permissions dangereuses, vérification des flags debuggable et allowBackup, détection des composants exportés.<br/>
<b>Technologies :</b> FastAPI, Uvicorn, Androguard, python-multipart

<h3 style="color:#1F618D;">Secret-Hunter (port 8002)</h3>
<b>Rôle :</b> Détection des secrets et informations sensibles codées en dur.<br/>
<b>Fonctionnalités :</b> Recherche de clés API, tokens OAuth, URLs Firebase et autres secrets dans les ressources et fichiers DEX.<br/>
<b>Technologies :</b> FastAPI, Uvicorn, Androguard

<h3 style="color:#1F618D;">Crypto-Check (port 8003)</h3>
<b>Rôle :</b> Analyse des mécanismes cryptographiques utilisés dans l’application.<br/>
<b>Fonctionnalités :</b> Détection des algorithmes faibles (MD5, SHA1) et des modes de chiffrement non sécurisés (AES ECB).<br/>
<b>Technologies :</b> FastAPI, Uvicorn, Androguard

<h3 style="color:#1F618D;">Network-Inspector (port 8004)</h3>
<b>Rôle :</b> Analyse des configurations réseau et de la sécurité des communications.<br/>
<b>Fonctionnalités :</b> Détection du trafic en clair, analyse des paramètres networkSecurityConfig et des URLs non sécurisées.<br/>
<b>Technologies :</b> FastAPI, Uvicorn, Androguard

<h3 style="color:#1F618D;">Report-Gen (port 8005)</h3>
<b>Rôle :</b> Centralisation et agrégation des résultats d’analyse.<br/>
<b>Fonctionnalités :</b> Génération de rapports structurés et calcul d’un niveau de risque global.<br/>
<b>Technologies :</b> FastAPI, Uvicorn

<h3 style="color:#1F618D;">Fix-Suggest (port 8006)</h3>
<b>Rôle :</b> Proposition de recommandations de correction.<br/>
<b>Fonctionnalités :</b> Suggestions de correctifs concrets et alignement avec OWASP MASVS.<br/>
<b>Technologies :</b> FastAPI, Uvicorn

<h3 style="color:#1F618D;">CI-Connector (port 8007)</h3>
<b>Rôle :</b> Orchestration des analyses dans un contexte CI/CD.<br/>
<b>Fonctionnalités :</b> Lancement automatisé des analyses et intégration avec GitHub Actions et GitLab CI.<br/>
<b>Technologies :</b> FastAPI, Uvicorn, Requests

<hr/>

<h2 style="color:#117864;">Prérequis techniques</h2>

<ul>
<li>Python 3.10 ou supérieur</li>
<li>Java JDK 11 ou 17 (nécessaire pour l’analyse des APK)</li>
<li>Git</li>
<li>Postman ou curl pour les tests API (optionnel)</li>
</ul>

<hr/>

<h2 style="color:#117864;">Installation et utilisation</h2>

Clonage du dépôt :
<pre>
git clone https://github.com/no3mane11/MobileSec_Projet.git
cd MobileSec_Projet
</pre>

Installation des dépendances principales :
<pre>
pip install fastapi uvicorn androguard python-multipart requests
</pre>

Lancement de tous les services en local :
<pre>
python master_launcher.py
</pre>

Les interfaces Swagger sont accessibles via :
http://127.0.0.1:8001/docs jusqu’à http://127.0.0.1:8007/docs

<hr/>

<h2 style="color:#117864;">Structure du projet</h2>

<pre>
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
</pre>

<hr/>

<h2 style="color:#117864;">Licence et contexte académique</h2>

Ce projet est distribué sous licence MIT et a été réalisé dans un cadre universitaire.  
Il vise à démontrer l’utilisation d’une architecture microservices pour l’analyse de sécurité des applications mobiles.

<i>
Une utilisation en production nécessiterait des mécanismes supplémentaires de sécurité, d’authentification et de montée en charge.
</i>

## 🎥 Simulation du projet
https://github.com/user-attachments/assets/7395e50d-27f5-4abd-a90a-00d706b1c287





