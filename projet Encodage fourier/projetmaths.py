#Imports
import json
import numba
import numpy as np





#Préparation des données
points = open('data.json')
donnéesjson = json.load(points)
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
nb_coeffs = 100
pasfourier=1000
coeffs=np.zeros(2*nb_coeffs+1,dtype=np.clongdouble)

#on calcule en tout 100 + 1 + 100 coefficients
#Transformée discrète par intégration numérique
for i in range(-nb_coeffs,nb_coeffs+1):
    def f(x):
        #renvoie une valeur pour x entre 0 et 1 en fonction de liste_points
        #on considère que cette fonction doit etre définie pour x multiple de 1/200000
        return liste_points[int(x*200000)]*np.exp(-2*np.pi*1j*i*x)
    coeffs[i]=integrer_trap(f,pasfourier,0,1)
    #a la position 0 on a coeff pour i = 0

#creation fichier json de sortie qui stocke les coeffs

    
  
import json,time
import cmath
import numpy as np
# Opening JSON file 
f = open('data.json') 
nbre=200
# returns JSON object as  
# a dictionary 
data = json.load(f)
  
# Iterating through the json 
# list 
listebourrin=[]
for i in data:  
    listebourrin.append(complex(i.get('x'),i.get('y')))
    
    
l = np.array(listebourrin)

# Closing file 
f.close()



pas = 0.1
#200 000 la taille de la liste
listedescn = []
for n in range(-nbre,nbre+1):
    res = 0
    for i in range(int(1/pas)):
        res+=pas* (l[i*20]) * cmath.exp(-2*cmath.pi*complex(0,1)*n*(pas*i))
    listedescn.append(res)



import numba,time
listedescn = coeffs

import pygame
pygame.init()

t=0
screen = pygame.display.set_mode([1400,800])
ablit = pygame.Surface((1400,800))
ablitv2 = pygame.Surface((1400,800))
running=True
print("FINI DE CHARGER")
linescoord=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

ablitv2.fill((255,255,255))
while running:
    time.sleep(0.001)
    t+=0.01
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
    
    laouafficher=0
    
    ablit.fill((255,255,255))
    
    N=0
    for n in range(0,nbre+1):
        lastadded=listedescn[n+nbre]*cmath.exp(complex(0,1)*n*t)
        laouafficher+=lastadded
        
        if(n<20):
        
            if(n==0):
                linescoord[N]=[0,0,lastadded.real,lastadded.imag]
            else:
                linescoord[N]=[linescoord[N-1][2],linescoord[N-1][3],linescoord[N-1][2]+lastadded.real,linescoord[N-1][3]+lastadded.imag]
            lll=linescoord[N]
            pygame.draw.line(ablit, (255,0,0), (lll[0], lll[1]), (lll[2], lll[3]))
            N+=1
        if(n!=0):
            n=-n
            lastadded=listedescn[n+nbre]*cmath.exp(complex(0,1)*n*t)
            laouafficher+=lastadded
            if(n>-20):
            
                
               
                linescoord[N]=[linescoord[N-1][2],linescoord[N-1][3],linescoord[N-1][2]+lastadded.real,linescoord[N-1][3]+lastadded.imag]
                lll=linescoord[N]
                pygame.draw.line(ablit, (255,0,0), (lll[0], lll[1]), (lll[2], lll[3]))
                N+=1
    
    
    
    
    
    
    

    pygame.draw.circle(ablitv2, (255,0,255), ((int(1*laouafficher.real),int(1*laouafficher.imag))), 2)
    
    
    
    ablit.set_colorkey((255,255,255))
    
    screen.blit(ablitv2,(0,0))
    screen.blit(ablit,(0,0))
    
    pygame.display.flip()
    
    
