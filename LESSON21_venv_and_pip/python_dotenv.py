# Voici comment python-dotenv fonctionne généralement :

#     Vous créez un fichier nommé .env dans le répertoire racine de votre projet (ou tout autre emplacement de votre choix).

#     Dans ce fichier .env, vous définissez les variables d'environnement avec leurs valeurs. Par exemple :

#     makefile

# API_KEY=your_api_key
# DATABASE_URL=your_database_url
# SECRET_KEY=your_secret_key

# Dans votre code Python, vous utilisez la bibliothèque python-dotenv pour charger ces variables d'environnement depuis le fichier .env. Voici un exemple de code pour le faire :

# python

#     from dotenv import load_dotenv

#     load_dotenv()  # Charge les variables d'environnement du fichier .env

#     import os

#     api_key = os.getenv("API_KEY")
#     db_url = os.getenv("DATABASE_URL")
#     secret_key = os.getenv("SECRET_KEY")

# En utilisant python-dotenv, vous pouvez garder votre configuration séparée 
# de votre code source, ce qui facilite la gestion des paramètres de configuration 
# spécifiques à l'environnement (développement, production, tests, etc.). 
# Cela simplifie également le processus de déploiement, 
# car vous pouvez avoir des fichiers .env différents pour chaque environnement 
# sans avoir à modifier le code lui-même.
