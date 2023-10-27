from random import choice

capital = "Topeka"
bird = "Westenr Meadowlark"
flower = "Sunflower"
song = "Home on the Range"

def randomfunfact():
    funfacts = [
        "Kansas is concidered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess that is Kansas City.",
        "A considerable portion of Kansas City is actually in Missouri.",
        "Most Kansans are annoyed by Wizard of Oz references from people outside of Kansas."
    ]

    index = choice("0123")
    
    print(funfacts[int(index)])
    
# Vérifie si le fichier Python est exécuté directement 
# et non importé en tant que module dans un autre script. 
# Si c'est le cas, il appelle la fonction randomfunfact().
if __name__ == "__main__":
    randomfunfact()

# Le bloc if __name__ == "__main__": sert à déterminer si le fichier actuel 
# est le point d'entrée principal du programme. Si c'est le cas, 
# les instructions à l'intérieur de ce bloc seront exécutées. 
# Cela permet souvent d'écrire du code qui peut être réutilisé en tant que module 
# (en l'important dans d'autres scripts) 
# tout en permettant également l'exécution indépendante du script en tant que programme autonome.

# Sans ce if, la fonction randomfunfact() serait lancée 2 fois au lancement de LESSON14_modules.py 
# 1 fois à cause de la ligne LESSON14_kansas.randomfunfact() de LESSON14_modules.py 
# et 1 fois à cause de son appel ligne 24 de ce fichier