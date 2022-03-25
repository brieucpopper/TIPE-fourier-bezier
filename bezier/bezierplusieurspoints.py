import pygame,time
pygame.init()
font = pygame.font.SysFont(None, 24)
img = font.render('Pressez Shift pour sélectionner deux points', True, (0,255,0))
img2=font.render('Pressez Entrée quand vous etes satisfaits\nCliquez pour changer le segment a controler', True, (0,255,0))


image = pygame.image.load('image.jpg')
def barycentre(avancement,p1,p2):
    return [int(avancement*p1[0]+(1-avancement)*p2[0]),int(avancement*p1[1]+(1-avancement)*p2[1])]
screen = pygame.display.set_mode([1000, 1000])
def affichervertpoints():
    for i in points:
        pygame.draw.circle(screen, (0, 255, 0), i, 3)
def afficher():
    
    screen.fill((255, 255, 255))
    screen.blit(image, (300, 300))
    for i in listepourafficher:
        
        pygame.draw.circle(screen, (0, 0, 0), i, 3)
def affichertxt():
    screen.blit(img, (20, 20))
    pygame.display.flip()

def affichertxt2():
    screen.blit(img2, (20, 20))
    pygame.display.flip()
def choixcourbe(p1,p2):
    v1=[0,0]
    v2=[0,0]
    v3=p1
    v4=p2
    choosing = True
    jemodifie1=True
    while choosing:
        
        res=[]
        screen.fill((255, 255, 255))
        afficher()
        affichertxt2()
        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), v1, 2)
        pygame.draw.circle(screen, (0, 0, 255), v2, 4)
        pygame.draw.circle(screen, (0, 0, 255), v3, 6)#on veut go de la
        pygame.draw.circle(screen, (0, 0, 255), v4, 8)# a la
        pygame.draw.line(screen,(0,0,0),v3,v2)
        pygame.draw.line(screen,(0,0,0),v4,v1)
        tauxech=600
        if(jemodifie1):
            v1=pygame.mouse.get_pos()
        else:
            v2=pygame.mouse.get_pos()
        for t in range(tauxech):
            #jen ai 3
            trois1,trois2,trois3=barycentre(t/tauxech,v4,v1),barycentre(t/tauxech,v1,v2),barycentre(t/tauxech,v2,v3)
            #pygame.draw.circle(screen, (0, 255, 255),trois1 , 1)
            #pygame.draw.circle(screen, (0, 255, 255),trois2 , 1)
            #pygame.draw.circle(screen, (0, 255, 255),trois3 , 1)

            #jen ai 2
            deux1,deux2=barycentre(t/tauxech,trois1,trois2),barycentre(t/tauxech,trois2,trois3)
            #pygame.draw.circle(screen, (0, 255, 255),deux1 , 1)
            #pygame.draw.circle(screen, (0, 255, 255),deux2 , 1)

            final=barycentre(t/tauxech,deux1,deux2)
            pygame.draw.circle(screen, (0, 0, 0),final , 5)
            res.append(final)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                jemodifie1=not jemodifie1
            if event.type==pygame.KEYDOWN:
                choosing=False
        
        pygame.display.flip()
        time.sleep(0.02)

        
    
    res2=(v1,v2,v3,v4)
    return (res,res2)



listeaexporter=[]
listepourafficher=[]
points=[]
while 1:
    afficher()
    affichervertpoints()
    affichertxt()
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                points.append(pygame.mouse.get_pos())
    if(len(points))==2:
        aaajouter=choixcourbe(points[0],points[1])
        for j in aaajouter[0]:
            listepourafficher.append(j)
        listeaexporter.append(aaajouter[1])
        print(listeaexporter)
        points=[]
        




                
                
    




        
        
        
        
    
    
