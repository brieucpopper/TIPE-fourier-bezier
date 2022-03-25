#Imports
import json
import numpy as np





#Préparation des données
points = open('data.json')
donnéesjson = json.load(points)
points.close()
nb_points = 200000

#Conversion des données en tableau numpy
liste_points = np.zeros(nb_points,dtype=np.clongdouble)
for i in range(nb_points):
    liste_points[i] = donnéesjson[i].get('x')+1j*donnéesjson[i].get('y')


#On a maintenant de quoi faire la transformée de Fourier discrète




#fonction d'intégration par la méthode des trapèzes

def integrer_trap(f,nbpas,debut,fin):
    res=0
    fagauche=f(debut)
    dx=(fin-debut)/nbpas

    for i in range(nbpas):
        fadroite=f(i*dx+debut)

        res+=(fagauche+fadroite)*dx/2
        fagauche=fadroite
    return res

#Paramètres de la transformée discrète
nb_coeffs = 300
pasfourier=3000
coeffs=np.zeros(300,dtype=np.clongdouble)

#on calcule en tout 100 + 1 + 100 coefficients
#Transformée discrète par intégration numérique
for i in range(0,nb_coeffs):
    def f(x):
        #renvoie une valeur pour x entre 0 et 1 en fonction de liste_points
        #on considère que cette fonction doit etre définie pour x multiple de 1/200000
        return liste_points[int(x*200000)]*np.exp(-2*np.pi*1j*i*x)
    coeffs[i]=integrer_trap(f,pasfourier,0,1)
    #a la position 0 on a coeff pour i = 0

#creation fichier json de sortie qui stocke les coeffs
with open('coeffs.json', 'w') as outfile:
    aenvoyer=[]
    for i in coeffs:
        aenvoyer.append(str(i))
    json.dump(aenvoyer,outfile)
    outfile.close()

print("L'encodage est fini!")








import pygame,time
nbbbbbbb=5000
def renvoiePointsDepuisCoeffs():
    coordpoints = np.zeros(nbbbbbbb,dtype=np.clongdouble)
    for t in range(nbbbbbbb):
        #on prend t par pas
        res=0
        for i in range(0,nb_coeffs):
            res=res+coeffs[i]*np.exp(i*1j*((t/nbbbbbbb)*2*np.pi))
        coordpoints[t]=res
    return(coordpoints)

pygame.init()
screen = pygame.display.set_mode([1400,800])
ablit = pygame.Surface((1400,800))
running=True

ablit.fill((255,255,255))
for i in renvoiePointsDepuisCoeffs():
        pygame.draw.circle(ablit, (0,0,0), ((int(i.real),int(i.imag))), 2)
        screen.blit(ablit,(0,0))
        pygame.display.flip()
    

        
    
