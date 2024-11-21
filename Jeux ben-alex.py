
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
running = True
position_personage = (100, 100)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (260, 0), 75)
    pygame.draw.ellipse(screen, (0, 0, 255), position_personage, 75)
    pygame.display.flip()       

pygame.quit()