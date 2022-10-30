from random import *

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
liste_P = [8,8,2,0,4,5]

def separation_polynome_paire_impaire(liste_P):
    liste_P_paire = []
    liste_P_impaire = []
    liste_P_finale = [] #liste de liste avec les deux du dessus

    for i in range (0, len(liste_P)-1, 2):
        liste_P_paire.append(liste_P[i])
        print(liste_P_paire)
        liste_P_impaire.append(liste_P[i+1])
        print(liste_P_impaire)
    
    liste_P_finale.append(liste_P_paire)
    liste_P_finale.append(liste_P_impaire)

    return liste_P_finale


############################################ EXECUTION #############################################

#print (Multiplication_Ecoleprimaire(3,4))

print(separation_polynome_paire_impaire(liste_P))