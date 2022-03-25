#Imports
import json
import numpy as np
import time



# DEBUT CODE POUR AFFICHER CLE DE SOL
#Préparation des données
points = open('data.json')
donnéesjson = json.load(points)
points.close()
nb_points = 200000

#Conversion des données en tableau numpy
liste_points = np.zeros(nb_points,dtype=np.clongdouble)
for i in range(nb_points):
    liste_points[i] = donnéesjson[i].get('x')+1j*donnéesjson[i].get('y')

#FIN CODE POUR AFFICHER CLE DE SOL

'''
files = open("data2.txt")
file_list =  files.readlines()


nb_points = len(file_list)
liste_points = np.zeros(nb_points,dtype=np.clongdouble)
for i in range(nb_points):
    ligne=file_list[i]

    liste_points[i]=int(ligne[0:3])-100+1j*int(ligne[4:7])-200j


''' #CODE A DECOMMENTER POUR AFFICHER "TIPE" a partir des donnees du fichier data2.txt



#On a maintenant de quoi faire la transformée de Fourier discrète



facteur=1
#fonction d'intégration par la méthode des trapèzes

def integrer_trap(f,nbpas,debut,fin):
    res=0
    fagauche=f(debut)
    dx=(fin-debut)/nbpas

    for i in range(1,nbpas):
        fadroite=f(i*dx+debut)

        res+=(fagauche+fadroite)*dx/2
        fagauche=fadroite
    res+=fadroite*dx
    return res
def f(x):
    return x
print(integrer_trap(f,400,0,1))
#Paramètres de la transformée discrète
nb_coeffs = 500
pasfourier=1000
coeffs=np.zeros(2*nb_coeffs+1,dtype=np.clongdouble)

#on calcule en tout 100 + 1 + 100 coefficients
#Transformée discrète par intégration numérique
for i in range(-nb_coeffs,nb_coeffs+1):
    def f(x):
        #renvoie une valeur pour x entre 0 et 1 en fonction de liste_points
        #on considère que cette fonction doit etre définie pour x multiple de 1/200000
        return liste_points[int(x*nb_points)]*np.exp(-2*np.pi*1j*i*facteur*x)
    modificateur=1
    coeffs[i+nb_coeffs]=integrer_trap(f,pasfourier*modificateur,0,1)
    #a la position 0 on a coeff pour i = 0
aeteenvoye=[]
#creation fichier json de sortie qui stocke les coeffs
with open('coeffs.json', 'w') as outfile:
    aenvoyer=[]
    for i in coeffs:
        aenvoyer.append(int(i.real*150))
        aenvoyer.append(int(i.imag*150))
    json.dump(aenvoyer,outfile)
    outfile.close()
    aeteenvoye=aenvoyer
print("L'encodage est fini!")

#on veut coeff de -100 a 0 a 100
#                 0      100 200



#fonction qui cree une liste de coeffs a partir d'un fichier
coeffs=[]

for i in range(0,len(aeteenvoye),2):
    coeffs.append(aeteenvoye[i]/150+1j*aeteenvoye[i+1]/150)



import pygame,time
nbbbbbbb=1000
def renvoiePointsDepuisCoeffs():
    coordpoints = np.zeros(nbbbbbbb,dtype=np.clongdouble)
    for t in range(nbbbbbbb):
        #on prend t par pas
        res=0
        for i in range(-nb_coeffs,nb_coeffs+1):
            
            res=res+coeffs[i+nb_coeffs]*np.exp(facteur*i*1j*((t/nbbbbbbb)*2*np.pi))
        coordpoints[t]=res
    return(coordpoints)

pygame.init()
screen = pygame.display.set_mode([1400,800])
ablit = pygame.Surface((1400,800))
running=True


pts=renvoiePointsDepuisCoeffs()



ablit.fill((255,255,255))
for i in pts:
        pygame.draw.circle(ablit,(0,0,0),(int(1*i.real),int(1*i.imag)),3)
screen.blit(ablit,(0,0))
pygame.display.flip()
time.sleep(1)



