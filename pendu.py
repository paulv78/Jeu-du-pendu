import random

#-----------OBTENIR UN MOT A TROUVER-----------#

#Ouvrir une liste des différents mots
with open("mots_pendu.txt",'r')as f:
    mots=f.read().split()


#Fonction choisir un mot aléatoire dans la liste
#-----------------------------------------------

def choisir_mot(mots):
    return random.choice(mots)

#Fonction choisir une lettre
#---------------------------

def choisir_une_lettre():
    lettre=input("entre la lettre que tu veux : ")
    if len(lettre)>1:                                #Si c'est pas une seule lettre, redemander une lettre et relancer la fonction
        print("rerentre une lettre")
        return choisir_une_lettre()
    else:                                            #Si y a bien qu'une seule lettre, retourner la lettre
        return lettre
    
#Fonction affichage mot à trou
#-----------------------------

def affichage_trou(mot,lettres_connus):
    mot_trou=""
    for lettre in mot:                 #Voir si et ou la lettre rentrée est dans le mot
        if lettre in lettres_connus:   #Si dedans, alors afficher la lettre à la position ou elle est
            mot_trou=mot_trou+lettre
        else:
            mot_trou=mot_trou+"_"      #Sinon, écrire un "_"
    return mot_trou


#--------MAINTENANT LE VRAI JEU COMMENCE--------#

def jeu():
    vie=6
    mot_a_trouver=choisir_mot(mots)
    lettres_connus=set()
    #for i in range(0,vie):   
    while vie>0:
        print(mot_a_trouver) #Pour pouvoir tester le code
        print("le mot à trouver est : "+ affichage_trou(mot_a_trouver,lettres_connus))
        print("il vous reste " + str(vie) + " vie.")

        lettre=choisir_une_lettre()

        if lettre in mot_a_trouver:
            print("Vous avez trouvé une lettre")
            lettres_connus.add(lettre)
            if set(mot_a_trouver) == lettres_connus:
                print("Bravo ! Vous avez gagné !")
                return
        else:
            print("Cette lettre n'est pas dans le mot")
            vie=vie-1

    print("perdu!, le mot à trouver étant : "+ mot_a_trouver)
    
jeu()

