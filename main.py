from random import *
from math import *
#from cmath import *
import cmath

#Fonction qui transforme un nombre en liste
def Nombre_Liste (nombre):
    x = []
    longueur_nombre = len(str(nombre))
    while longueur_nombre != 0:
        longueur_nombre = longueur_nombre - 1
        x.append(int(str(nombre)[longueur_nombre]))
    return x

# [int(random()*10) for i in range (n)] pour avoir un nombre aléatoire de taille n

#1. Algorithme naïf

#Soient x,y deux nombres de taille n
def Multiplication_Ecoleprimaire (x,y):

    # "taille" des nombres
    t1 = len(str(x))
    t2 = len(str(y))
    
    # nombres sous forme de liste
    nb1_liste = Nombre_Liste(x)
    nb2_liste = Nombre_Liste(y)

    # boucle pour les multiplications
    for i in range (t1):
        for j in range (t2):
          nb1_liste[i]*nb2_liste[j]  

# polynome 8 + 8x + 2x² + 0x^3 + 4x^4 + 5x^5
liste_P = [8,6,2,0,4,5,1,2]

# fonction pour avoir les polynomes P^(i) et P^(p)
def separation_polynome_paire_impaire(liste_P):
    liste_P_paire = []
    liste_P_impaire = []
    liste_P_finale = [] #liste de liste avec les deux du dessus

    for i in range (0, len(liste_P)-1, 2):
        liste_P_paire.append(liste_P[i])
        liste_P_paire.append(0)
        #print(liste_P_paire)
        liste_P_impaire.append(0)
        liste_P_impaire.append(liste_P[i+1])
        #print(liste_P_impaire)
    
    liste_P_finale.append(liste_P_paire)
    liste_P_finale.append(liste_P_impaire)

    return liste_P_finale


# fonction pour générer les 2n racines de l'unité
def racines_un(n):
    liste_racines = []
    # n c'est la longueur du polynôme donc degré n-1

    for k in range (2*n):
        w = cmath.exp((2*pi)/(2*n) * 1j * k)
        #print (w)
        liste_racines.append(w)

    #print(k)
    return liste_racines


# fonction pour évaluer un polynôme en ces 2n racines de l'unité
def FFT1(P, c):     # on dit que P c'est une liste c'est plus pratique
    # si c = 1 on fait toute la liste * z
    # si c = 0 on fait rien
    liste_racine_unite = []
    liste_racine_unite = racines_un(len(P))     # on récupère le nombre de racines de l'unité voulu
    liste_polynome_evalue = []      # liste retournée à la fin

    for o in range (len(liste_racine_unite)):       # on met déjà x_0 partout pcq ça dépend pas de w
        liste_polynome_evalue.append(liste_P[0])
    #print (liste_polynome_evalue)

    for k in range (len(liste_racine_unite)):       # de 0 à 2n-1
        w = liste_racine_unite[k]       # une des racines de l'unité
        w2 = w*w     # pour avoir z²

        for i in range (1,len(P)):        # de 0 à n-1
            x = P[i]        # x indice i  
            w2_puissance_i = cmath.exp(w2 * cmath.log(i))
            liste_polynome_evalue[k]  = liste_polynome_evalue[k] + x * w2_puissance_i     # P(w) = x_0 * w^0 + x_1 * w^1 + ...
                  
        if c == 1:
            for s in range (len(liste_polynome_evalue)):
                liste_polynome_evalue[s] = liste_polynome_evalue[s] * w

    return liste_polynome_evalue


# fonction qui scinde le polynome en deux et évalue et tout et tout
def FFT2(P):
    liste_polynomes_separes = separation_polynome_paire_impaire(P)
    liste_polynome_paire_evalue = []
    liste_polynome_impaire_evalue = []

    liste_polynome_paire_evalue = FFT1(liste_polynomes_separes[0], 0)
    liste_polynome_impaire_evalue = FFT1(liste_polynomes_separes[1], 1)

    print(liste_polynome_paire_evalue)
    print(liste_polynome_impaire_evalue)

    #for k in range (liste_polynome_paire_evalue):






############################################ EXECUTION #############################################

#print (Multiplication_Ecoleprimaire(3,4))

#print(separation_polynome_paire_impaire(liste_P))

#print (racines_un(10))

print(FFT2(liste_P))