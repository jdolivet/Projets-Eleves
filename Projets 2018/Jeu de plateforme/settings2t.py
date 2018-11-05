import pygame as pg

#DETERMINATION DES COULEURS
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

#PARAMETRES DU JEU
TITRE = "jeux"
LARGEUR = 1000
HAUTEUR = 560
FPS = 60
gravite = 0.8


TILESIZE = 32

#AIRE DU JOUER
PLAYER_HIT_RECT = pg.Rect(0, 0, 30, 30)
#IMAGES UTILISEES
ENNEMY_IMG='feu.png'
PLAYER_IMG='feu.jpg'
MARCHE_AVANT1="player_walk1.png"
MARCHE_AVANT2 = 'player_kick.png'
MARCHE_AVANT3 = 'player_walk2.png'
IMOBILE_IMG="player_idle.png"
SAUTE_IMG = 'player_jump.png'
MARCHE_ARRIERE="marche_arriere.jpg"
VIE_IMG='vie.png'
