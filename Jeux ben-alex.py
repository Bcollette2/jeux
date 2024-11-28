
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

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), position_cercle, 75)
    position_cercle = (position_cercle[0], position_cercle[1]+0.005)
    screen.blit(personage, position_personage)
    pygame.display.flip()       

pygame.quit()

def Random (chiffre):
    randint = random.random()
return randint * chiffre 


