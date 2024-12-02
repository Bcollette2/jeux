import pygame
import random

pygame.init()
clock = pygame.time.Clock()
TAILLEECRAN = [500, 700]
fps = 60
screen = pygame.display.set_mode(TAILLEECRAN)
running = True
personage = pygame.image.load("./IMG_3545.png").convert_alpha()
personage = pygame.transform.scale(personage, (50, 80))
vies = 3
personage2 = pygame.image.load("./IMG_3546.png").convert_alpha()
personage2 = pygame.transform.scale(personage2, (50, 80))
vies2 = 3
position_personage = (100, 500)
position_personage2 = (300, 500)
position_rectangle = (260, 0)
position_rectangle2 = (340, 0)
coeur = pygame.image.load("./IMG_3547.png").convert_alpha()
coeur = pygame.transform.scale(coeur, (50, 50))


def rrandom(chiffre):
    randint = random.random()
    return randint * chiffre


def nouvelleobstacle(position_balle):
    if position_balle[1] >= 500:
        return True
    else:
        return False

font = pygame.font.Font(None, 32)
text = font.render('Garçon a gagné. R pour recommencer', True, (0, 0, 128), (128, 0, 0))
text2 = font.render('Fille a gagné. R pour recommencer', True, (0, 0, 128), (128, 0, 0))
gars = font.render('Vies Gars', True, (0, 0, 128))
fille = font.render('Vies Fille', True, (0, 0, 128))
runningRight = False
runningLeft = False
runningRight2 = False
runningLeft2 = False
point = 0
while running:
    point += 1
    points = font.render('points: r'+ str(point), True, (0, 0, 128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type ==   pygame.KEYDOWN:
            if event.key == pygame.K_a:
                runningRight = True
            elif event.key == pygame.K_d:
                runningLeft = True
            elif event.key == pygame.K_LEFT:
                runningRight2 = True
            elif event.key == pygame.K_RIGHT:
                runningLeft2 = True
            elif event.key == pygame.K_r:
              vies = 3
              vies2 = 3
              point = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                runningRight = False
            elif event.key == pygame.K_d:
                runningLeft = False
            elif event.key == pygame.K_LEFT:
                runningRight2 = False
            elif event.key == pygame.K_RIGHT:
                runningLeft2 = False
    if runningLeft and position_personage[0] < 450:
        position_personage = (position_personage[0] + 8, position_personage[1])
    elif runningRight and position_personage[0] > 0:
        position_personage = (position_personage[0] - 8, position_personage[1])
    if runningLeft2 and position_personage2[0] < 450:
        position_personage2 = (position_personage2[0] + 8, position_personage2[1])
    elif runningRight2 and position_personage2[0] > 0:
        position_personage2 = (position_personage2[0] - 8, position_personage2[1])
    rectanglejoueur1 = pygame.Rect(position_personage[0], position_personage[1], 50, 80)
    rectanglejoueur2 = pygame.Rect(position_personage2[0], position_personage2[1], 50, 80)
    rectangle2 = pygame.Rect(position_rectangle[0], position_rectangle[1], 75, 75)
    rectangle3 = pygame.Rect(position_rectangle2[0], position_rectangle2[1], 75, 75)
    if rectanglejoueur1.colliderect(rectangle2):
        position_rectangle = (rrandom(700), 0)
        vies -= 1
    if rectanglejoueur2.colliderect(rectangle2):
        position_rectangle = (rrandom(700), 0)
        vies2 -= 1
    if rectanglejoueur1.colliderect(rectangle3):
        position_rectangle2 = (rrandom(700), 0)
        vies -= 1
    if rectanglejoueur2.colliderect(rectangle3):
        position_rectangle2 = (rrandom(700), 0)
        vies2 -= 1
    screen.fill((255, 255, 255))
    if nouvelleobstacle(position_rectangle):
        position_rectangle = (rrandom(700), 0)
    if nouvelleobstacle(position_rectangle2):
        position_rectangle2 = (rrandom(700), 0)
    pygame.draw.rect(
        screen, (0, 0, 255), (position_rectangle[0], position_rectangle[1], 75, 75)
    )
    pygame.draw.rect(
        screen, (0, 0, 255), (position_rectangle2[0], position_rectangle2[1], 75, 75)
    )
    position_rectangle = (position_rectangle[0], position_rectangle[1] + 10.5)
    position_rectangle2 = (position_rectangle2[0], position_rectangle2[1] + 10.5)
    screen.blit(personage, position_personage)
    screen.blit(personage2, position_personage2)
    if vies <= 0:
        screen.blit(text2, (100, 200))

    elif vies2 <= 0:
        screen.blit(text, (100, 200))
    if vies == 1:
        screen.blit(coeur, (0, 20))
    elif vies == 2: 
        screen.blit(coeur, (0, 20))
        screen.blit(coeur, (40, 20))
    elif vies == 3: 
        screen.blit(coeur, (00, 20))
        screen.blit(coeur, (40, 20))
        screen.blit(coeur, (80, 20))
    if vies2 == 1:
        screen.blit(coeur, (380, 20))
    elif vies2 == 2: 
        screen.blit(coeur, (420, 20))
        screen.blit(coeur, (380, 20))
    elif vies2 == 3: 
        screen.blit(coeur, (380, 20))
        screen.blit(coeur, (460, 20))
        screen.blit(coeur, (420, 20))
    screen.blit(gars, (0, 0))
    screen.blit(fille, (400, 0))
    screen.blit(points, (200, 10))
    pygame.display.flip()
    clock.tick(fps)
