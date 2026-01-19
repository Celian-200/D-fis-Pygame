import pygame, sys
from pygame.locals import QUIT


pygame.init()

largeur, hauteur = 800, 600

fenetre = pygame.display.set_mode((largeur, hauteur))

couleur_fond = "#0061ff"
couleur_carte = "#60efff"

# Variables de jeu
carte_largeur = 100
carte_hauteur = 100
emplacement_carte = 10

while True :
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    fenetre.fill(couleur_fond)
    pygame.display.update()
