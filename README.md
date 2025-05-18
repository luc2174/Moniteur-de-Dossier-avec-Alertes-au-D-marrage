Ce script Python permet de surveiller en temps réel un dossier spécifique sur votre ordinateur (par défaut C:\Your-Path). À chaque modification, création ou suppression de fichier dans ce dossier, une notification est automatiquement envoyée sur un webhook Discord.

De plus, le script envoie également une alerte lors du démarrage de l’ordinateur, vous permettant de savoir quand la machine est allumée.

Fonctionnalités principales
🔍 Surveillance en temps réel d’un dossier local, avec prise en charge récursive (sous-dossiers inclus)

📩 Notifications instantanées sur Discord pour chaque événement : création, modification ou suppression de fichier

🖥️ Alerte au démarrage du PC pour notifier que la machine est allumée

🚀 Exécution automatique au démarrage de Windows via placement dans le dossier shell:startup

⚙️ Facile à configurer en modifiant le chemin du dossier surveillé et l’URL du webhook Discord

🛠️ Possibilité de compiler en fichier .exe autonome avec pyinstaller

Prérequis
Python 3.x installé sur votre machine

Modules Python : requests et watchdog

pip install requests watchdog
Installation et utilisation
Modifier le script pour remplacer l’URL du webhook Discord par la vôtre.

Modifier le chemin du dossier à surveiller si besoin (WATCHED_FOLDER dans le script).

Lancer le script manuellement pour tester son fonctionnement.

(Optionnel) Compiler en .exe pour exécuter sans installer Python :


pyinstaller --onefile --noconsole monitor.py
Placer le fichier .exe dans le dossier shell:startup pour démarrer automatiquement avec Windows :

Touche Windows + R

Tapez shell:startup et validez

Copiez-collez l’.exe dans ce dossier

Exemple d’utilisation
Surveillance d’un dossier partagé

Suivi des modifications importantes dans un dossier personnel

Notification instantanée pour la sécurité ou le monitoring à distance

Avertissements
Ce script doit être exécuté avec des droits suffisants pour accéder au dossier surveillé.

Pour la notification au démarrage, assurez-vous que le script démarre bien avec Windows (dossier shell:startup).

La fréquence d’alerte dépend des actions effectuées sur les fichiers du dossier.
