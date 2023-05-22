import random

#-----------OBTENIR UN MOT A TROUVER-----------#

#Ouvrir une liste des différents mots
with open("mots_pendu.txt",'r')as f:
    mots=f.read().split()


#Fonction choisir un mot aléatoire dans la liste
#-----------------------------------------------

def choisir_mot(mots):                      #Fonction prenant en entrée la liste entière des mots et retournant un seul mot choisi aléatoirement
    return random.choice(mots)

#Fonction choisir une lettre
#---------------------------

def choisir_une_lettre():
    lettre=input("entre la lettre que tu veux : ")
    if len(lettre)>1:                                #Si il y a plus d'une seule lettre, redemander une lettre et relancer la fonction
        print("rerentre une lettre")
        return choisir_une_lettre()
    else:                                            #Si y a bien qu'une seule lettre, retourner la lettre
        return lettre                                #Renvois la lettre
    
#Fonction affichage mot à trou
#-----------------------------

def affichage_trou(mot,lettres_connus):     #Fonction prenant en entrée le mot et l'ensemble des lettres ayant été trouvées
    mot_trou=""                        #initialisation de mot_trou
    for lettre in mot:                 #Voir si et ou la lettre rentrée est dans le mot
        if lettre in lettres_connus:   #Si elle est dedans, alors afficher la lettre à la position ou elle est
            mot_trou=mot_trou+lettre
        else:
            mot_trou=mot_trou+"_"      #Sinon, écrire un "_"
    return mot_trou                    #Retourne le mot avec seulement les lettres connues de révélé


#--------MAINTENANT LE VRAI JEU COMMENCE--------#

def jeu():
    vie=6           #Initialisation du compteur de vie à 6
    mot_a_trouver=choisir_mot(mots)    #Utilisation de la fonction permettant de sélectionner un mot au hasard dans la liste proposé dans le fichier mots_pendu.txt
    lettres_connus=set()       #Initialisation de la liste des lettres connues
    while vie>0:   #Boucle "tant que" le nombre de vie est suppérieur à 0
        #print(mot_a_trouver) #Cette ligne sert à pouvoir tester le code
        print("le mot à trouver est : "+ affichage_trou(mot_a_trouver,lettres_connus))  #Utilisation de la fonction affichage_trou
        print("il vous reste " + str(vie) + " vie.")      #Affiche à l'utilisateur le nombre de vie restant

        lettre=choisir_une_lettre()    #Utilisation de la fonction permettant la rentrée par l'utilisateur d'une lettre

        if lettre in mot_a_trouver:                    #Si la lettre rentrée est dans le mot
            print("Vous avez trouvé une lettre")
            lettres_connus.add(lettre)                  #Ajouter cette lettre à la liste des lettres connues
            if set(mot_a_trouver) == lettres_connus:    # Si le mot correspond aux lettres trouvées
                print("Bravo ! Vous avez gagné !")
                return                                  #Fin de la boucle et de la partie
        else:                                            #Sinon
            print("Cette lettre n'est pas dans le mot")
            vie=vie-1                                    #Diminue de 1 le compteur de vie

    print("perdu!, le mot à trouver étant : "+ mot_a_trouver)  #Afficher le mot qu'il fallait trouver
    
jeu()   #lancer le jeu

