import pygame
import random
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
personage = pygame.image.load('./IMG_3545.png').convert_alpha()
personage = pygame.transform.scale(personage, (50, 80))
print(personage)
position_personage = (100, 400)
position_cercle = (260, 0)
def rrandom(chiffre):
    randint = random.random()
    return randint * chiffre 

def tempsattack(tempsattack):
  if tempsattack < 500:
    return True
  else :
      return False 
def nouvelleballe(position_balle):
    if position_balle[1] >= 500:
        return True
    else:
        return False
runningRight = False
runningLeft = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                runningRight = True
                print('m')
                print(event.type)
            elif event.key == pygame.K_d:
                runningLeft = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                runningRight = False
            elif event.key == pygame.K_d:
                runningLeft = False
    if (runningLeft and position_personage[0] <450):
        position_personage = (position_personage[0] + 1, position_personage[1])
        print(position_personage)
    elif runningRight and position_personage[0] > 0:
        position_personage =                            (position_personage[0] -                      1, position_personage[1])
    screen.fill((255, 255, 255))
    if nouvelleballe(position_cercle):
        position_cercle = (rrandom(500), 0)
    pygame.draw.circle(screen, (0, 0, 255), position_cercle, 75)
    position_cercle = (position_cercle[0], position_cercle[1]+0.5)
    screen.blit(personage, position_personage)
    pygame.display.flip()       



