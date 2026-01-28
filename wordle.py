import random

mots = ["chat", "vide", "rose"]
mot_ordi = random.choice(mots)
mot_joueur = ""

while mot_ordi != mot_joueur : 
    mot_joueur = str(input("Chosis un mot : "))
    c1 = mot_joueur[0]
    c2 = mot_joueur[1]
    c3 = mot_joueur[2]
    c4 = mot_joueur[3]

    if mot_ordi == mot_joueur :
        print("Gagné")
    elif c1 or c2 or c3 or c4 in mot_ordi :
        if c1 in mot_ordi and c1 == mot_ordi[0] :
            print("Le caractère : ", c1, "est correctement placé")
        elif c1 in mot_ordi :
            print("Le caractère : ", c1, "est bon mais mal placé.")
        if c2 in mot_ordi and c2 == mot_ordi[1] :
            print("Le caractère : ", c2, "est correctement placé")
        elif c2 in mot_ordi :
            print("Le caractère : ", c2, "est bon mais mal placé.")
        if c3 in mot_ordi and c3 == mot_ordi[2] :
            print("Le caractère : ", c3, "est correctement placé")
        elif c3 in mot_ordi :
            print("Le caractère : ", c3, "est bon mais mal placé.")
        if c4 in mot_ordi and c4 == mot_ordi[3] :
            print("Le caractère : ", c4, "est correctement placé")
        elif c1 in mot_ordi :
            print("Le caractère : ", c4, "est bon mais mal placé.")
    else :
        print("Aucun caractère correct !")   