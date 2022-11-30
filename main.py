from random import *
from math import *
from cmath import *


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


# polynome 8 + 6x + 2x² + 0x^3 + 4x^4 + 5x^5 + 1x^6 + 2x^7
liste_P_x = [8,6,2,0,4,5,1,2]
#print(liste_P_x)
# polynome avec les coefficients dans l'autre sens
liste_P_y = [2,1,5,4,0,2,6,8]
#print(liste_P_y)


## 2.2.2
# fonction pour avoir les polynomes P^(i) et P^(p)
def separation_polynome_paire_impaire(liste_P):
    liste_P_paire = []
    liste_P_impaire = []
    liste_P_finale = [] #liste de liste avec les deux du dessus

    for i in range (0, len(liste_P)-1, 2):
        liste_P_paire.append(liste_P[i])
        liste_P_impaire.append(liste_P[i+1])
    
    liste_P_finale.append(liste_P_paire)
    liste_P_finale.append(liste_P_impaire)

    return liste_P_finale


## 2.2.3
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



"""# fonction pour évaluer un polynôme en ces 2n racines de l'unité
def FFT(P, c):     # on dit que P c'est une liste c'est plus pratique
    # si c = 1 on fait toute la liste * z
    # si c = 0 on fait rien
    liste_racine_unite = racines_un(len(P))     # on récupère le nombre de racines de l'unité voulu
    liste_polynome_evalue = []      # liste retournée à la fin

    for o in range (len(liste_racine_unite)):       # on met déjà x_0 partout pcq ça dépend pas de w
        liste_polynome_evalue.append(P[0])
    #print (liste_polynome_evalue)

    for k in range (len(liste_racine_unite)):       # de 0 à 2n-1 (pour toutes les racines unité on évalue le polynome en ces racines)
        w = liste_racine_unite[k]       # une des racines de l'unité
        w2 = w*w     # pour avoir z² comme dans l'énoncé

        for i in range (1,len(P)):        # de 0 à n-1 (pour tous les coeff du polynome à part le 0, mais traité avant donc oklm)
            x = P[i]        # x_i
            # on fait w^(2i) (en passant à l'exponentielle sinon ça marche pas avec les complexes jsp pq)  
            w2_puissance_i = cmath.exp(i * cmath.log(w2))       
            liste_polynome_evalue[k]  = liste_polynome_evalue[k] + x * w2_puissance_i     # P(w) = x_0 * w^0 + x_1 * w^1 + ...

        """ """
        Ici en vrai je fais des calculs en trop pcq pour le polynome paire les indices impaires c'est 0
        Et donc je calcule w²^i  pour rien et j'ajoute à ma liste pour rien
        Mais ça évite de faire deux méthodes FFT donc je laisse par flemme
        """"""
                  
        if c == 1:      # si c'est la liste du polynome impaire faut faire tout * z (ici z = w)
            for s in range (len(liste_polynome_evalue)):
                liste_polynome_evalue[s] = liste_polynome_evalue[s] * w

    # à la fin c'est une liste avec pour chaque case, le polynome évalué en une des 2n racines de l'unité ( *z si c'est P^(i) )
    return liste_polynome_evalue



# fonction qui scinde le polynome en deux et évalue et tout et tout
def FFT_finale(P):
    liste_polynomes_separes = separation_polynome_paire_impaire(P)
    liste_polynome_paire_evalue = []
    liste_polynome_impaire_evalue = []
    liste_polynome_evalue = []

    liste_polynome_paire_evalue = FFT(liste_polynomes_separes[0], 0)
    liste_polynome_impaire_evalue = FFT(liste_polynomes_separes[1], 1)
    """ """
    donc là on a chaque liste avec le polynome évalué en les 2n racines de l'unité
    i.e. les deux parties de l'addition suivante
    P(z) = P^(p)(z) + zP^(i)(z)
    on additionne tout membre à membre et c'est ok on aura ce qu'on veut
    """"""
    
    # print pour tester
    #print(liste_polynome_paire_evalue)
    #print(liste_polynome_impaire_evalue)

    for k in range (len(liste_polynome_paire_evalue)):       # ils doivent faire la même longueur donc c'est ok de mettre ça
        liste_polynome_evalue.append( liste_polynome_paire_evalue[k] + liste_polynome_impaire_evalue[k] )

    return liste_polynome_evalue
    """

# méthode FFT
def FFT(P):
    
    n = len(P)      # n = longueur de P

    """polynome_P_I = separation_polynome_paire_impaire(P)     # on sépare le polynome en deux
    polynome_P = polynome_P_I[0]        # le 1er de la piste est paire
    polynome_I = polynome_P_I[1]        # le 2nd de la liste est impaire"""

    if n==1:
        return P

    else:
        polynome_P_I = separation_polynome_paire_impaire(P)     # on scinde le polynome en deux
        polynome_P = polynome_P_I[0] 
        polynome_I = polynome_P_I[1] 
        
        y_P = FFT(polynome_P)       # partie récursive
        y_I = FFT(polynome_I)       # on rappelle la méthode pour rescinder les polynomes
    
        w = np.exp(-2j * np.pi * np.arange(n) / n)      # liste avec tous les w^(qqch) pour évaluer après
        
        y1 = y_P + w[:int(n/2)] * y_I
        y2 = y_P + w[int(n/2):] * y_I
        y = np.concatenate([y1, y2])        # on concatene les listes comme il faut
    
        return y

########################

## 2.2.4

def mult(P,Q):
    
    n = len(P)
    
    FFT_P = FFT(P)
    FFT_Q = FFT(Q)
    PQ = [0]*(2*n-1)
    
    for i in range (n):
        for j in range (n):
            m = FFT_P[i] * FFT_Q[j]
            PQ[i+j] = m + PQ[i+j]
            
    return PQ
    
    
# 2.3.1   
def IFFT(P):
       
    n = len(P)      # n = longueur de P

    """polynome_P_I = separation_polynome_paire_impaire(P)     # on sépare le polynome en deux
    polynome_P = polynome_P_I[0]        # le 1er de la piste est paire
    polynome_I = polynome_P_I[1]        # le 2nd de la liste est impaire"""

    if n==1:
        return P

    else:
        polynome_P_I = separation_polynome_paire_impaire(P)     # on scinde le polynome en deux
        polynome_P = polynome_P_I[0] 
        polynome_I = polynome_P_I[1] 
        
        y_P = FFT(polynome_P)       # partie récursive
        y_I = FFT(polynome_I)       # on rappelle la méthode pour rescinder les polynomes
    
        w = np.exp(2j * np.pi * np.arange(n) / n)/n      # liste avec tous les w^(qqch) pour évaluer après
        print("oui")
        y1 = y_P + w[:int(n/2)] * y_I
        y2 = y_P + w[int(n/2):] * y_I
        y = np.concatenate([y1, y2])        # on concatene les listes comme il faut
    
        return y   

############################################ EXECUTION #############################################

#print (Multiplication_Ecoleprimaire(3,4))

#print(separation_polynome_paire_impaire(liste_P_x))
#print(separation_polynome_paire_impaire(liste_P_y))

#print (racines_un(10))

#print (FFT(liste_P,0))

#print (FFT_finale(liste_P_x))
#print (FFT_finale(liste_P_y))

print ("-------------------------------------------------------------------------------")
#print (FFTrecursif(liste_P_x))
#print(mult_Px_Py(liste_P_x,liste_P_y))
print(FFTinternet(liste_P_y))
print ("-------------------------------------------------------------------------------")
