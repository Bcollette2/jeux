
import pygame
import random
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
personage = pygame.image.load('./IMG_3545.png').convert_alpha()
personage = pygame.transform.scale(personage, (50, 80))
print(personage)
position_personage = (100, 100)
position_cercle = (260, 0)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.K_LEFT:
            position_personage[0] = position_personage[0] - 10
        elif event.key == pygame.K_RIGHT:
            position_personage[0] = position_personage[0] + 10
    if nouvelleballe(position_cercle) = True:
        position_cercle = (Random(),0)
    
   
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), position_cercle, 75)
    position_cercle = (position_cercle[0], position_cercle[1]+0.005)
    screen.blit(personage, position_personage)
    pygame.display.flip()       

pygame.quit()

def Random (chiffre):
    randint = random.random()
    return randint * chiffre 

def tempsattack (tempsattack):
  if tempsattack < 500:
    tempsattack = return True
  else :
      return False 
def nouvelleballe (position_balle):
    if position_balle[1] >= 500:
        return True
    else:
        return False
    


