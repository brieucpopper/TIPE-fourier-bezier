
import pygame
pygame.init()
screen = pygame.display.set_mode([1000, 1000])
listepourafficher=[]

files = open("databezierlettreR.txt")
file_list =  files.readlines()
file_list2=[(int(i[1:4]),int(i[6:9]))for i in file_list]
def barycentre(avancement,p1,p2):
    return [int(avancement*p1[0]+(1-avancement)*p2[0]),int(avancement*p1[1]+(1-avancement)*p2[1])]
screen = pygame.display.set_mode([1000, 1000])   

def reconstituer(v1,v2,v3,v4):
    tauxech=600
    res=[]
    for t in range(tauxech):
            
            trois1,trois2,trois3=barycentre(t/tauxech,v4,v1),barycentre(t/tauxech,v1,v2),barycentre(t/tauxech,v2,v3)
            
            deux1,deux2=barycentre(t/tauxech,trois1,trois2),barycentre(t/tauxech,trois2,trois3)
            

            res.append(barycentre(t/tauxech,deux1,deux2))
    return res
print(file_list[0])
for i in range(0,len(file_list),4):
    for j in reconstituer(file_list2[i],file_list2[i+1],file_list2[i+2],file_list2[i+3]):
        listepourafficher.append(j)
def afficher():
    
    screen.fill((255, 255, 255))
    for i in listepourafficher:
        
        pygame.draw.circle(screen, (0, 0, 0), i, 3)

while 1:
    
    afficher()
    pygame.display.flip()
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
