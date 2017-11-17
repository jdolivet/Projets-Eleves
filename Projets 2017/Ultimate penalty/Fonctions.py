import pygame
import os
import random

width = 1000
height = 800
centre_x = width/2
centre_y = height/2
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Les fichiers où se situent les images et les sons
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
sound_folder = os.path.join(game_folder, "sound")

# Images
bg = pygame.image.load(os.path.join(img_folder, "bgblanc.jpg")).convert()
flèchedroite = pygame.image.load(os.path.join(img_folder, "flèchedroite.png")).convert()
flèchegauche = pygame.transform.flip(flèchedroite, 1, 0)
jouer = pygame.image.load(os.path.join(img_folder, "Jouer.png")).convert_alpha()
rejouer = pygame.image.load(os.path.join(img_folder, "Rejouer.png")).convert_alpha()
but = pygame.image.load(os.path.join(img_folder, "BUT.png")).convert()
image_son = pygame.image.load(os.path.join(img_folder, "Hautparleur.jpg")).convert()
image_pas_son = pygame.image.load(os.path.join(img_folder, "PasHautparleur.jpg")).convert()
image_infinie = pygame.image.load(os.path.join(img_folder, "infinie.jpg")).convert()
image_pasinfinie = pygame.image.load(os.path.join(img_folder, "pasinfinie.jpg")).convert()

# Fonction pour ecrire sur l ecran
def draw_text(surf, text, size, x, y, color = black):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# Fonction pour déterminer la précision et les coordonées du mouvement du ballon
def Précision(précision, direction, sy, sx):

    Bonne_direction = 1 * précision
    Moyenne_direction = (3 - précision) * précision
    Mauvaise_direction = (3 - précision) * 0.5
    Tir_pr = (random.choices([3, 2, 1], [Bonne_direction, Moyenne_direction, Mauvaise_direction]))


    Tir_précision = Tir_pr


    if Tir_précision == [3]:
        if 1 <= direction <= 3:
            sy = -21
        if 4 <= direction <= 6:
            sy = -16
        if direction == 1 or direction == 4:
            sx = -10
        if direction == 3 or direction == 6:
            sx = 10
        if direction == 2 or direction == 5:
            sx = 0

    if Tir_précision == [2]:
        if 1 <= direction <= 3:
            sy = -21
        if 4 <= direction <= 6:
            sy = -16
        if direction == 1 or direction == 4:
            sx = -10
        if direction == 3 or direction == 6:
            sx = 10
        if direction == 2 or direction == 5:
            sx = 0

    if Tir_précision == [1]:
        sy = random.choice([-10, 10, -5, 5])
        sx = random.choice([-10, 10, -5, 5])

    return [sx, sy, Tir_précision, direction]

# Fonction pour déterminer où le gardien va sauter
def sautgardien(force, Tir_précision, direction):
    gardienstop = False
    if Tir_précision == [1]:
        if force == 1 or force == 2:
            st = ["Immobile"]
        if force == 3:
            st = (random.choices(["PeuImporte", "Immobile"], [0.5, 0.5]))

    if Tir_précision == [2]:
        if force == 1:
            st = ["Bon"]
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.25, 0.75]))
        if force == 3:
            st = (random.choices(["Mauvais", "Bon"], [0.65, 0.35]))

    if Tir_précision == [3]:
        if force == 1:
            st = (random.choices(["Mauvais", "Bon"], [0.60, 0.40]))
        if force == 2:
            st = (random.choices(["Mauvais", "Bon"], [0.8, 0.2]))
        if force == 3:
            st = ["Mauvais"]

    if st == ['Immobile']:
        saut = 0
        gardienstop = True

    elif st == ['Mauvais'] or st == ["PeuImporte"]:
        if direction == 1:
            saut = random.choice([2, 3, 4, 5, 6])
        elif direction == 2:
            saut = random.choice([1, 3, 4, 5, 6])
        elif direction == 3:
            saut = random.choice([1, 2, 4, 5, 6])
        elif direction == 4:
            saut = random.choice([1, 2, 3, 5, 6])
        elif direction == 5:
            saut = random.choice([1, 2, 3, 4, 6])
        elif direction == 6:
            saut = random.choice([1, 2, 3, 4, 5])

    elif st == ['Bon']:
        saut = direction

    return [saut, gardienstop, st]


