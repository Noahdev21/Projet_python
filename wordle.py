import random
mots4 = [
    "abri","acte","aide","aile","aime","aire","ami","ange","arme","avis",
    "bain","banc","base","beau","bebe","bien","bois","bord","bras","brun",
    "cage","camp","cash","cave","ceci","cela","chef","chez",
    "ciel","clef","clou","coin","cola","coup","cour","cube",
    "dame","dans","date","deux","doux","dure",
    "echo","elle","etre",
    "face","faim","fait","faux","film","fils","fini","flot","fond","font",
    "gare","gens","gout","gras","gris",
    "haut","hier","hors",
    "idee","ilot","issu",
    "jean","joie","jour","juge",
    "kilo",
    "lait","lame","lent","lien","lire","logo","loin","long","lune",
    "main","mais","male","mari","menu","midi","mine","mode","mois",
    "nage","neuf","noir","note",
    "obus","onde",
    "pain","pair","parc","part","pate","peur","pile","plan","plat","plie",
    "plus","pont","port","pose","pour","prix",
    "quoi",
    "rage","rare","rire","robe","rond","rose","roue",
    "sale","sang","saut","site","soin","soir","sort","sous",
    "tard","taxi","tire","tout","tour","truc","type",
    "vent","vers","vite","voix","vole","vote",
    "yoga",
    "zinc","zone"]
mots5 = [
    "abris","actes","aides","aimer","aires","aller","amour","anges","armes","assez",
    "bains","barbe","bases","basse","beaux","boire","bruit","brume","bulle","buter",
    "cable","calme","canal","carte","cause","cette","chose","clair","corps","coups",
    "danse","dates","debut","dents","diner","doute","droit","duree","eclat","ecole",
    "elles","ennui","entre","faire","femme","fleur","foire","force","forme",
    "geste","givre","grand","guide","habit","haute","heure","hiver","homme",
    "image","jambe","jeune","jouer","laver","livre","lourd","lutte","mains",
    "mange","marie","match","merci","mieux","monde","morte","neige","noire","notre",
    "ordre","paire","passe","payer","peine","plein","porte","poser","quand","reste"
]
mots6 = [
    "abords","accord","adulte","affect","aidera","aimait","airbus","ajoute","animal",
    "baiser","ballon","banque","barque","besoin","billet","boites","bureau","butter",
    "cacher","calmer","camion","canard","carnet","chance","charge","choisi","classe","combat",
    "danser","decide","degres","demain","devoir","doigts","donner","douter","droite",
    "ecrire","effort","eleves","emploi","enfant","entrer","espace",
    "facile","femmes","fermer","fleurs","fondre","former","fouler","foudre",
    "gagner","garage","garder","glacer","gouter","grande","groupe","habits","hasard","hautes",
    "ideale","images","jamais","jouets","lancer","lettre",
    "maigre","manger","marche","mettre","milieu","minute","montee","moteur","nature"
]
mot_joueur = ""
mode = 0
nom_joueur = str(input("Salut, nouveau joueur, quel est ton nom ? "))
print("Bienvenue ", nom_joueur,"tu vas pouvoir jouer à ce wordle. Le but est simple : tu dois réussir à trouver le mot de l'ordinateur en proposant diverses mots. Tu as la possibilté de choisir différents paramètres : ")
mode = int(input("Tu dispose d'un mode classique, d'un mode vie limités et d'un mode compétitif. Si tu souhaites connaître les détails de chaque mode tape 0 sinon tapes 1, 2 ou 3 pour choisir : "))
while mode == 0 :
    print("Le mode classique est un mode ou tu devras trouver le mot de manière normale sans vie et avec des assistances limitées. Le mode vie limitées quant à lui est un mode ou tu devras réussir à trouver le bon mot en un nombre d'essai limités ! Pour finir le mode compétitif est un mode ou tu devras deviner le mot tout en gagnant un maximum de points.")
    mode = int(input("Alors souhaites-tu le mode classique, vies limités ou compétitif ? Tapes 1, 2 ou 3 : "))
while mode not in (1, 2, 3) :
    mode = int(input("Alors souhaites-tu le mode classique, vies limités ou compétitif ? Tapes 1, 2 ou 3 : "))
if mode == 1 :
    niveau = int(input("Choisis ton niveau de difficulté de 1 à 3 : "))
    if niveau == 1 :
        mot_ordi = random.choice(mots4)
        print("Attention ! Le mot que tu devras trouver est de 4 caractères. Bonne chance", nom_joueur, "!")
        while mot_ordi != mot_joueur :
            mot_joueur = str(input("Choisis un mot : "))
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
                elif c4 in mot_ordi :
                    print("Le caractère : ", c4, "est bon mais mal placé.")
            else :
                print("Aucun caractère correct !")   
    elif niveau == 2 :
        mot_ordi = random.choice(mots5)
        print("Attention ! Le mot que tu devras trouver est de 5 caractères. Bonne chance", nom_joueur, "!")
        while mot_ordi != mot_joueur : 
            mot_joueur = str(input("Choisis un mot : "))
            c1 = mot_joueur[0]
            c2 = mot_joueur[1]
            c3 = mot_joueur[2]
            c4 = mot_joueur[3]
            c5 = mot_joueur[4]

            if mot_ordi == mot_joueur :
                print("Gagné")
            elif c1 or c2 or c3 or c4 or c5 in mot_ordi :
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
                elif c4 in mot_ordi :
                    print("Le caractère : ", c4, "est bon mais mal placé.")
                if c5 in mot_ordi and c5 == mot_ordi[4] :
                    print("Le caractère : ", c5, "est correctement placé")
                elif c5 in mot_ordi :
                    print("Le caractère : ", c5, "est bon mais mal placé.")
            else :
                print("Aucun caractère correct !")
    elif niveau == 3 :
        mot_ordi = random.choice(mots6)
        print("Attention ! Le mot que tu devras trouver est de 6 caractères. Bonne chance", nom_joueur, "!")
        while mot_ordi != mot_joueur : 
            mot_joueur = str(input("Choisis un mot : "))
            c1 = mot_joueur[0]
            c2 = mot_joueur[1]
            c3 = mot_joueur[2]
            c4 = mot_joueur[3]
            c5 = mot_joueur[4]
            c6 = mot_joueur[5]

            if mot_ordi == mot_joueur :
                print("Gagné")
            elif c1 or c2 or c3 or c4 or c5 or c6 in mot_ordi :
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
                elif c4 in mot_ordi :
                    print("Le caractère : ", c4, "est bon mais mal placé.")
                if c5 in mot_ordi and c5 == mot_ordi[4] :
                    print("Le caractère : ", c5, "est correctement placé")
                elif c5 in mot_ordi :
                    print("Le caractère : ", c5, "est bon mais mal placé.")
                if c6 in mot_ordi and c6 == mot_ordi[5] :
                    print("Le caractère : ", c6, "est correctement placé")
                elif c6 in mot_ordi :
                    print("Le caractère : ", c6, "est bon mais mal placé.")
            else :
                print("Aucun caractère correct !")