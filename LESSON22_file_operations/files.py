# Lancer (.venv) PS C:\Users\Sandra\Documents\mini_projects_python\LESSON22_file_operations> py files.py

# CRUD :
# r = Read
# a = Append
# w = Write
# x = Create

import os

##############################################################
# Read - error if file doesn't exist

# f = open("names.txt", "rt") for a text file
# f = open("names.txt", "rb") for a binary file ...
# f = open("names.txt", "r") for any file without precision bur "r" is optional = default action
f = open("names.txt")
# print(f.read())

# print(f.read(6))
# ne fonctionne pas : curseur à la fin du fichier
# car il vient d'être lu avec le print précédent
# si print précédent commenté, on obtiens : Sandra (6 caractères)

# Pour lire seulement la 1ère ligne :
# print(f.readline())
# Sandra

# Si ajout d'un second readline, lecture de le 2nde ligne
# print(f.readline())
# Jane

# Parcourir et imprimer chaque ligne
for line in f:
    print(line)
# Sandra
#
# Jane 
#     
# Eddie
#
# Jimmy
# line.strip() pour supprimer les lignes vides entre chaque nom

# Toujours fermer le fichier après lecture
# pour éviter de le modifier par erreur
f.close()

try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()
# The file you want to read doesn't exist

##############################################################
# Append : create the file if it doesn't exist 

f = open("names.txt", "a")
f.write("Dave\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()
# Sandra
# Jane
# Eddie
# Jimmy
# Dave (à la ligne si ligne vide à la fin du fichier txt, sinon collé à Jimmy)

##############################################################
# Write (overwrite)
f = open("context.txt", "w")
f.write("I delete all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()
# I delete all of the context

##############################################################
# Two ways to create a new file

# Open a file for writing, create the file if it does not exist
f = open("names_list.txt", "w")
f.close()
# création d'un fichier names_list.txt

# Create the specified file, but returns an error if the file exists
if not os.path.exists("sandra.txt"):
    f = open("sandra.txt", "x")
    f.close()
# création d'un fichier sandra.txt

##############################################################
# Delete a file

# Avoid an error if it doesn't exist
if os.path.exists("sandra.txt"):
    os.remove("sandra.txt")
else:
    print("The file you wish to delete not exist")
# supprime le fichier sandra.txt si il existe   

##############################################################
# Copier liste de more_names.txt dans names.txt
with open("more_names.txt") as f:
    content = f.read()

# with open("names.txt") as f:
#     f.write(content)
# io.UnsupportedOperation: not writable    
with open("names.txt", "w") as f:
    f.write(content)
# remplace le contenu de names.txt par celui de more_names.txt
# Dave n'existe plus









