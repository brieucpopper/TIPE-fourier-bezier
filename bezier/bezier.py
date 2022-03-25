# Simple pygame program

# Import and initialize the pygame library
import pygame,time
pygame.init()


v1=[200,100]
v2=[100,100]
v3=[450,500]
v4=[550,500]

def barycentre(avancement,p1,p2):
    return [int(avancement*p1[0]+(1-avancement)*p2[0]),int(avancement*p1[1]+(1-avancement)*p2[1])]


# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
running = True
jemodifie1=True
while running:
    
    if(jemodifie1):
        v1=pygame.mouse.get_pos()
    else:
        v2=pygame.mouse.get_pos()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            jemodifie1=not jemodifie1
    
    # Fill the background with white
    screen.fill((255, 255, 255))
    
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), v1, 2)
    pygame.draw.circle(screen, (0, 0, 255), v2, 4)
    pygame.draw.circle(screen, (0, 0, 255), v3, 6)#on veut go de la
    pygame.draw.circle(screen, (0, 0, 255), v4, 8)# a la
    pygame.draw.line(screen,(0,0,0),v3,v2)
    pygame.draw.line(screen,(0,0,0),v4,v1)
    tauxech=1000
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
        
        

        
    time.sleep(0.01)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
