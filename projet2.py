import random

nombre = random.randint(1, 100)
nbrsuppose = None

while nbrsuppose != nombre:
    nbrsuppose = int(input("Choisir un nombre entre 1 et 100: "))
    
    if nbrsuppose > nombre:
        print("Trop élevé !")
    elif nbrsuppose < nombre:
        print("Trop bas !")
    else:
        print("Correcte !")
        choix = input("Entrez votre choix (1 pour recommencer ou 2 pour quitter) : ")
        
        if choix == '1':
            nombre = random.randint(1, 100) 
            nbrsuppose = None 
            print("Vous pouvez recommencer le jeu \n")
        elif choix == '2':
            print("Vous avez quitté le jeu")
            break 
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.\n")
