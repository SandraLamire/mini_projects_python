# pip = prefered intallation programme (pour pouvoir installer des packages)

# Installation globale = dans le terminal : 
# py -m pip install requests (ou pip install --user requests si Accès refusé)

# ajouter chemin vers python + vers Scripts dans python (pour pip): setx PATH "%PATH%;C:\Users\Sandra\AppData\Local\Programs\Python\Python311\Scripts"
# dans powershell admin si message :
#  WARNING: The scripts pip.exe, pip3.11.exe and pip3.exe are installed in 
# 'C:\Users\Sandra\AppData\Local\Programs\Python\Python311\Scripts' which is not on PATH.

# py -m pip list (liste les applications installées en global sur le pc)
        # Package            Version
        # ------------------ ---------
        # certifi            2023.7.22
        # charset-normalizer 3.3.1
        # idna               3.4
        # pip                23.3.1
        # requests           2.31.0
        # setuptools         65.5.0
        # urllib3            2.0.7

# Mettre à jour
# py -m pip install --upgrade pip

# Installer 1 version spécifique
# py -m pip install requests==2.30.0

# Mettre à jour un package
# py -m pip install -U requests
# py -m pip install -U pip  (MAJ pip)

# Supprimer un package
# py -m pip uninstall requests

# Installer un environnement pour un projet
# (pour le dev mais pas dans git et github)
# py -m venv .venv
# lancer l'environnement ( = terminal affiche (.venv) PS C:\...)
#  . .\.venv\Scripts\Activate
# Si message d'erreur : pas les droits
# Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
# py -m venv .venv
# Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope Process
# ou désactiver antivirus
# ensuite installer et exécuter des packages Python dans cet environnement virtuel de manière isolée
# pip install nomDeChaquePackageUtileAuProjet (pour ce projet : pip install requests)

# Charger des variables d'environnement à partir d'un fichier .env dans un projet
# garde la configuration séparée du code
# pip install python-dotenv

# Python packages Index = Aller sur https://pypi.org/ pour trouver des packages

# afficher la liste des packages installés dans l'environnement virtuel
# pip freeze
# sauvegarder cette liste dans un fichier pour gestion des dépendances
# pip freeze > requirements.txt

# Dans projet, créer un nouveau fichier .gitignore pour exclure .venv de git
# en y écrivant : .venv


# désactiver l'environnement virtuel et 
# revenir à l'environnement Python système par défaut
# deactivate

# Voir les détails d'un package
# py -m pip show requests













