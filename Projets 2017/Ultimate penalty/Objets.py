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

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
sound_folder = os.path.join(game_folder, "sound")

#Les Images

class Terrain(pygame.sprite.Sprite):
   #sprite for the player
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Terrain.jpg")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width / 2, height / 2)

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Intro.jpg"))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

class ExitImage(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "Team1.jpg"))
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)

# Les figures

class Gardien(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.loadimages()
       self.image = self.Milieu
       self.rect = self.image.get_rect()
       self.rect.center = (width / 2, height / 3.5)
       self.droite = False
       self.lastupdate = 0
       self.saut = 0
       self.speedy = 0
       self.speedx = 0
       self.accelerationx = 0
       self.accelerationy = 0
       self.goal = False
       self.stop = False

   def loadimages(self):
       self.Milieu = pygame.image.load(os.path.join(img_folder, "Gardien0.png")).convert_alpha()
       self.Haut_a_gauche = pygame.image.load(os.path.join(img_folder, "Gardien1.png")).convert_alpha()
       self.Bas_a_gauche = pygame.image.load(os.path.join(img_folder, "Gardien4.png")).convert_alpha()
       self.Bas_a_droite = pygame.transform.flip(self.Bas_a_gauche, 1, 0)
       self.Haut_a_droite = pygame.transform.flip(self.Haut_a_gauche, 1, 0)
       self.Bas_milieu = self.Milieu # on a pas réussi a trouvé des images pour sauter vers le haut
       self.Haut_milieu = self.Milieu # on a pas réussi a trouvé des images pour sauter vers le bas

       self.centergauchehaut = (310, 230)
       self.centerdroitehaut = (650, 230)
       self.centerdroitebas = (580, 320)
       self.centergauchebas = (310, 320)

   def animate(self):
       self.loadimages()
       if self.saut != [0]:
           if self.saut == [1]:
               self.speedy = -2.95
               self.speedx = -20
               self.image = self.Haut_a_gauche
           if self.saut == [2]:
               self.image = self.Haut_milieu
               self.stop = True
           if self.saut == [3]:
               self.speedy = -3.73
               self.speedx = 20
               self.image = self.Haut_a_droite
           if self.saut == [4]:
               self.speedy = 9.7
               self.speedx = -20
               self.image = self.Bas_a_gauche
           if self.saut == [5]:
               self.image = self.Bas_milieu
               self.stop = True
           if self.saut == [6]:
               self.speedy = 23
               self.speedx = 20
               self.image = self.Bas_a_droite

       self.speedy += self.accelerationy
       self.speedx += self.accelerationx
       self.rect.y += self.speedy
       self.rect.x += self.speedx


       # --------- POUR QUE LE GARDIEN ARRETE SON MOUVEMENT-----------
       if self.rect.y >= 230 and self.rect.x <= 420: #( BAS A GAUCHE)
           self.rect.center = self.centergauchebas
           self.accelerationy = -9.7
           self.accelerationx = 20
           self.stop = True
       if self.rect.y >= 230 and self.rect.x >= 450: #( BAS A DROITE)
           self.rect.center = self.centerdroitebas
           self.accelerationy = -23
           self.accelerationx = -20
           self.stop = True
       if self.rect.y <= 200 and self.rect.x <= 310: #( HAUT A GAUCHE)
           self.rect.center = self.centergauchehaut
           self.accelerationy = 2.95
           self.accelerationx = 20
           self.stop = True
       if self.rect.y <= 200 and self.rect.x >= 650: #( HAUT A DROITE)
           self.rect.center = self.centerdroitehaut
           self.accelerationy = 3.73
           self.accelerationx = -20
           self.stop = True

class Ballon(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.ballon = pygame.image.load(os.path.join(img_folder, "Ballon.png")).convert()
       self.image = self.ballon
       self.image.set_colorkey(white)
       self.rect = self.image.get_rect()
       self.rect.center = (500, 580)
       self.speedy = 0
       self.speedx = 0
       self.sy = 0
       self.sx = 0
       self.accy = 0
       self.accx = 0
       self.stop = False
       self.width = 75
       self.height = 78

    def update(self):
       self.rect.y += self.speedy + self.accy
       self.rect.x += self.speedx + self.accx

       if self.rect.y <= 0 or self.rect.y >= 800 or self.rect.x <= 0 or self.rect.x >= 1000:
           self.kill()
           self.stop = True

        # ----------------------------------------------- POUR QUE LE BALLON S'ARRETE -------------------------------------------------
       if self.rect.y <= 135 and self.rect.x >= 650: #( EN HAUT A DROITE)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == 10 and self.sy == -21:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

       if self.rect.y <= 135 and self.rect.x <= 290: #( EN HAUT A GAUCHE)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == -10 and self.sy == -21:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

       if self.rect.y <= 290 and self.rect.x <= 290: #( EN BAS A GAUCHE)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == -10 and self.sy == -16:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

       if self.rect.y <= 280 and self.rect.x >= 630: #( EN BAS A DROITE)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == 10 and self.sy == -16:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

       if self.rect.y <= 270 : #( EN BAS AU MILIEU)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == 0 and self.sy == -16:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

       if self.rect.y <= 120 : #( EN HAUT AU MILIEU)
           # ( if avec les sx et sy pour un tir moyen)
           if self.sx == 0 and self.sy == -21:
               self.accx = -self.speedx
               self.accy = -self.speedy
               self.stop = True

    def diminuer(self, force):
        if force == 1:
            self.width = self.width / 1.017
            self.height = self.height / 1.017
        if force == 2:
            self.width = self.width / 1.02
            self.height = self.height / 1.02
        if force == 3:
            self.width = self.width / 1.025
            self.height = self.height / 1.025

        self.image = pygame.transform.scale(self.ballon, (int(self.width), int(self.height)))

class Player(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "player.png"))
       self.rect = self.image.get_rect()
       self.rect.center = (width / 3.5, height / 1.2)
       self.run = False
       self.speedy = 0
       self.speedx = 0
       self.chute = pygame.image.load(os.path.join(img_folder, "playerchute.png"))
       self.chutant = False
       self.accy = 0
       self.accx = 0

   def update(self):

       if self.run == True:
           self.speedx = 20
           self.speedy = -20

       if self.rect.x >= 400 and self.rect.y <= 600:
           self.image = self.chute
           self.chutant = True
           self.accy = -self.speedy
           self.accx = -self.speedx
       self.rect.x += self.speedx + self.accx
       self.rect.y += self.speedy + self.accy

# Pour mesurer La Force et déterminer la direction

class BarredeForce(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Barre_de_force.png")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (800, height/2)

class BarredePrécision(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Rectangle_de_précision_Pénalti.jpg")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width/2, height/1.2)

class FlèchedeForce(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_force.png")).convert()
       self.rect = self.image.get_rect()
       self.image.set_colorkey(white)
       self.rect.center = (842, 515)
       self.force_déterminée = False  # Pendant que le button est appuyé
       self.bouton_déjà_appuyé = False # Pour que le button ne soit plus appuyé à nouveau
       self.force = 0

   def update(self):
       self.speedy = 0
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_SPACE] and not self.force_déterminée:
           self.speedy = -10 + self.acceleration_y
           self.bouton_déjà_appuyé = True
       self.rect.y += self.speedy
       if self.rect.top < 215:
           self.rect.center = (842, 515)
       if self.rect.top >400:
           self.acceleration_y = 0
           self.force = 1
       if 400>self.rect.top >350:
           self.acceleration_y = -5
           self.force = 2
       if 350>self.rect.top >220:
           self.acceleration_y = -10
           self.force = 3
       if  not keystate[pygame.K_SPACE] and self.bouton_déjà_appuyé: # Ne fonctionne que si b == True, donc que si on a déjà avant
           self.force_déterminée = True

class FlèchedePrécision(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load(os.path.join(img_folder, "Flèche_de_précision.png")).convert()
       self.rect = self.image.get_rect()
       self.rect.center = (width/2, height/1.2)
       self.acceleration_x = 0
       self.vitesseinitiale = 15
       self.précision = 0

   def update(self):
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_SPACE]:
           self.acceleration_x = self.vitesseinitiale
       self.speedx = -self.vitesseinitiale + self.acceleration_x
       self.rect.x += self.speedx
       if self.rect.left < 400:
           self.acceleration_x = 2 * self.vitesseinitiale
       if self.rect.right > 600:
           self.acceleration_x = 0
       if  (490, height/1.2) <= self.rect.center <= (510, height/1.2):
           self.précision = 3
       if  (460, height/1.2) <= self.rect.center < (490, height/1.2) or (510, height/1.2) < self.rect.center <= (540, height/1.2):
           self.précision = 2
       if (420, height / 1.2) <= self.rect.center < (460, height / 1.2) or (540, height / 1.2) < self.rect.center <= (580, height / 1.2):
           self.précision = 1
       if  (390, height/1.2) <= self.rect.center < (420, height/1.2) or (580, height/1.2) < self.rect.center <= (610, height/1.2):
           self.précision = 0
