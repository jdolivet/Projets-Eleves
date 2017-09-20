##################  A.I.L.F.  ####################
import csv
import sys
import time


#### DEFINITIONS ----------------------- ####


def Convertie(liste, mode):
    """ Cette fonction convertie une liste en chaine de caractere ou vice versa. Dépendant du besoin dans la fonction.
"""
    liste = str(liste)
    if mode is list:
        liste = liste.split(' ')
    elif mode is str:
        liste = str(liste)
    return(liste)

#

def Compteur():
    """ Cette fonction est un compteur de bonnes ou mauvaises chose qu'on dit au programme.

"""
    global compteur


    for el in Trait[3]:
        if el is not '':
            if el in phrase:
                compteur += -1
                break


        
    for el in Trait[4]:
        if el is not '':
            if el in phrase:
                compteur += 1
                break

#

def Simplification(Liste):
    """ Cette fonction simplifie la phrase avant la recherche de mots clefs pour la rendre exploitable.
    Elle enleve: ponctuation, majuscule
"""
    Liste = RemplaceCaractere(Liste, Trait[0], ' ')
    Convertie(Liste, str)
    for el in Trait[1]:
        if el in Liste:
            a = Trait[1].index(el)
            caract = Trait[2][a] 
            Liste = RemplaceCaractere(Liste,Trait[1][a],Trait[2][a])

    return(Liste)


#


def RemplaceCaractere(Liste1,Liste2,Caract) :
    """ Cette fonction remplace les caracteres de la Liste1 present dans la Liste2.
par un espace ou par le Caract.
    Liste1 est une chaine de caractere,
    et Liste2 une liste.
"""
    Liste1 = Convertie(Liste1, str)
    for i in range(len(Liste1)):
        for el in Liste1[i]:
            if el in Liste2:
                Liste1 = Liste1.replace(el, Caract)
    return(Liste1)

#


def RechercheMotClef(Liste):
    """Cette fonction identifie les mots clefs de la phrase par rapport au
tableau des mots clefs. Puis 
"""
    global phrase

    Compteur()    
    Convertie(Liste, list)
    
    i=0
    j=0

    
            
    #
    if 'revoir' in Liste:
        phrase += "'Arrete'"
        return(Liste)
    #    
    for a in Tab[0]:
        if a in Liste:
            i= Tab[0].index(a)
    for b in range(1,40):
        if Tab[b][0] in Liste:
            j=b
    #

    Reponse(i,j)



#

def print_slow(str,mode):
    """
"""
    if mode is 1:
        for  letter in "Ailf:":
            sys.stdout.write (letter)  
    time.sleep(.7)
    for letter in str:
        sys.stdout.write (letter)  
        time.sleep(.01)
    print()    
    


#

def Reponse(x,y):
    """Cette fonction identifie une reponse a partir de coordonnees.
"""
    global compteur

    if compteur is -3:
        print_slow(" Vous n'etes pas tres sympa.",1)
        compteur=0
    if compteur is 3:
        print_slow(" Merci.",1)
        compteur=0
    
    else:
        if Rep[y][x]is 'X':
            print_slow( "J'ai pas compris" , 1)            
        else:
            print_slow( Rep[y][x] , 1)
            

    
        


#### VARIABLES ----------------------- ####


phrase = ()
compteur = 0


###  Introduction  ###


csv_in = open('tab.csv', 'r')                   #import des tableau
myreader = csv.reader(csv_in, delimiter=';')
Tab = list(myreader)

csv_in = open('Reponses.csv', 'r') 
myreader = csv.reader(csv_in, delimiter=',')
Rep = list(myreader)

csv_in = open('Triage.csv', 'r') 
myreader = csv.reader(csv_in, delimiter=';')
Trait = list(myreader)

###  Programme  ###

print_slow(" LE PROGRAMME NE COMPREND PAS LES ACCENTS.",0)     #introduction
print(" -----------------------------------------")
print_slow(" Tu veux une presentation?",1)
phrase = input("Vous: ").replace("'"," ").split(" ")

if "oui" in phrase:
    print_slow(" Bonjour, je m’appelle AILF.",1)
    print_slow("Je suis un grand spécialiste de tennis.",0)
    print_slow("T’as un doute sur ce sport magnifique?",0)
    print_slow("Si oui, pose moi une question.",0)
    print_slow("Vas-y, ne sois pas timide.",0)
else:
    print_slow("OK",1)

while "Arrete" not in phrase:                                   #boucle
    phrase = input("Vous: ").replace("'"," ").split(" ")
    phrase = Simplification(phrase)
    RechercheMotClef(phrase)
    
csv_in.close()
