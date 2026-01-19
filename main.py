import pygame, sys
from pygame.locals import QUIT
import time
pygame.init()

fenetre = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Mon personnage avec Pygame')

FPS = 60
horloge = pygame.time.Clock()
horloge.tick(FPS)
# Les fonctions
def dessiner() :
    fenetre.fill("#6D9699")

    pygame.draw.rect(fenetre, "#AAAAAA", (50, 10, 200, 250))
    pygame.draw.ellipse(fenetre, "#FF0000", (60, 170, 180, 80))
    pygame.draw.rect(fenetre, "#0008FF", (50, 10, 200, 250), 5)
    pygame.draw.circle(fenetre, "#000000", (200,60), 40, 15)
    pygame.draw.circle(fenetre, "#000000", (100,60), 40, 15)
    pygame.draw.line(fenetre, "#000000", (160, 120), (150, 150), 15)
    pygame.draw.ellipse(fenetre, "#000000", (60, 170, 180, 80), 4)
    pygame.draw.rect(fenetre, "#FFFFFF", (100, 180, 100, 20))
    pygame.draw.rect(fenetre, "#FFFFFF", (100, 220, 100, 20))
    pygame.draw.rect(fenetre, "#FFF000", (130, 180, 20, 20))
    pygame.draw.rect(fenetre, "#FFF000", (180, 180, 20, 20))
    pygame.draw.rect(fenetre, "#FFF000", (160, 220, 20, 20))
    pygame.draw.rect(fenetre, "#FFF000", (110, 220, 20, 20))



    pygame.display.update()
while True :
    temps = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        dessiner()
        horloge.tick(FPS)
