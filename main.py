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
    for i in range (4):
        print (i)




############################################ EXECUTION #############################################

print (Multiplication_Ecoleprimaire(3,4))