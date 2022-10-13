
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
    n = len(str(x))
print ("test")
