import pygame
import random

pygame.init()
clock = pygame.time.Clock()
fps = 600
screen = pygame.display.set_mode([500, 500])
running = True
personage = pygame.image.load("./IMG_3545.png").convert_alpha()
personage = pygame.transform.scale(personage, (50, 80))
vies = 3
personage2 = pygame.image.load("./IMG_3546.png").convert_alpha()
personage2 = pygame.transform.scale(personage2, (50, 80))
vies2 = 3
position_personage = (100, 400)
position_personage2 = (300, 400)
position_rectangle = (260, 0)


def rrandom(chiffre):
    randint = random.random()
    return randint * chiffre


def tempsattack(tempsattack):
    if tempsattack < 500:
        return True
    else:
        return False


def nouvelleobstacle(position_balle):
    if position_balle[1] >= 500:
        return True
    else:
        return False

font = pygame.font.Font(None, 32)
text = font.render('Garçon a gagné. R pour recommencer', True, (0, 0, 128), (128, 0, 0))
text2 = font.render('Fille a gagné. R pour recommencer', True, (0, 0, 128), (128, 0, 0))
runningRight = False
runningLeft = False
runningRight2 = False
runningLeft2 = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                runningRight = True
            elif event.key == pygame.K_d:
                runningLeft = True
            elif event.key == pygame.K_LEFT:
                runningRight2 = True
            elif event.key == pygame.K_RIGHT:
                runningLeft2 = True
        elif event.type == pygame.K_r:
            vies = 3
            vies2 = 3
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
        position_personage = (position_personage[0] + 1, position_personage[1])
    elif runningRight and position_personage[0] > 0:
        position_personage = (position_personage[0] - 1, position_personage[1])
    if runningLeft2 and position_personage2[0] < 450:
        position_personage2 = (position_personage2[0] + 1, position_personage2[1])
    elif runningRight2 and position_personage2[0] > 0:
        position_personage2 = (position_personage2[0] - 1, position_personage2[1])
    rectanglejoueur1 = pygame.Rect(position_personage[0], position_personage[1], 50, 80)
    rectanglejoueur2 = pygame.Rect(position_personage2[0], position_personage2[1], 50, 80)
    rectangle2 = pygame.Rect(position_rectangle[0], position_rectangle[1], 75, 75)
    if rectanglejoueur1.colliderect(rectangle2):
        position_rectangle = (rrandom(500), 0)
        vies -= 1
    if rectanglejoueur2.colliderect(rectangle2):
        position_rectangle = (rrandom(500), 0)
        vies2 -= 1
    screen.fill((255, 255, 255))
    if nouvelleobstacle(position_rectangle):
        position_rectangle = (rrandom(500), 0)
    pygame.draw.rect(
        screen, (0, 0, 255), (position_rectangle[0], position_rectangle[1], 75, 75)
    )
    position_rectangle = (position_rectangle[0], position_rectangle[1] + 0.5)
    screen.blit(personage, position_personage)
    screen.blit(personage2, position_personage2)
    if vies <= 0:
        screen.blit(text2, (100, 200))
    elif vies2 <= 0:
        screen.blit(text, (100, 200))
    pygame.display.flip()
    clock.tick(fps)
