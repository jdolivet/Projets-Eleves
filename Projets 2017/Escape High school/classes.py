import pygame
from Reglages import *
import pytmx
from Fonctions import *
from random import randint
import math


class Joueur(pygame.sprite.Sprite):
    def __init__(self, jeu, x, y):
        pygame.sprite.Sprite.__init__(self, jeu.tout_sprites)
        self.imagedevant = pygame.image.load("charfront.png")
        self.imagearrière = pygame.image.load("char_back.png")
        self.image = self.imagearrière
        self.rect = pygame.Surface.get_rect(self.image)
        self.x_initial =x
        self.y_initial = y
        self.x = x
        self.rect.x = x
        self.y = y
        self.rect.y = y
        self.vel_y = 0
        self.vel_x = 0
        self.ancienne_porte = 0
        self.jeu = jeu


    def mouvement(self):
        self.vel_x = 0  #varaible commence toujours a 0 car le personnage est imobile a chaque update
        self.vel_y = 0

        apertado = pygame.key.get_pressed()      #fonction pygame pour verifier si la touche est appuyee
        if apertado[pygame.K_w]:
            self.vel_y = -3         #se deplace de 3 pixels
            self.image = self.imagearrière #affiche image du dos du personnage
        if apertado[pygame.K_a]:
            self.vel_x = -3
        if apertado[pygame.K_s]:
            self.vel_y = 3
            self.image = self.imagedevant    #affiche image du perrsonnage vu de face
        if apertado[pygame.K_d]:
            self.vel_x = 3

    def collision(self, direction):
        if direction == 'x':
            collision_eleves = pygame.sprite.spritecollide(self,self.jeu.liste_eleves,False)   #fonction pygame pour voir si rectangle du personage touche un autre rectangle
            collision = pygame.sprite.spritecollide(self, self.jeu.obstacles_sprites, False)  #fonction pygame pour voir si rectangle du personage touche un autre rectangle
            if collision or collision_eleves:  # test de collision pour axe abscisses
                self.x -= self.vel_x            #revient a la derniere coordonne avant la collision
                self.vel_x = 0                  #si il y a colllision, alors il arrete de se deplacer
                self.rect.x = self.x            #coordonnees du joueur prennent les valeurs d avant la collision
        if direction == 'y':
            collision_eleves = pygame.sprite.spritecollide(self, self.jeu.liste_eleves, False)
            collision = pygame.sprite.spritecollide(self, self.jeu.obstacles_sprites, False)
            if collision or collision_eleves:  #teste de collision pour axe des ordonnees
                self.y -= self.vel_y           #revient a la derniere coordonne avant la collision
                self.vel_y = 0                 #si il y a colllision, alors il arrete de se deplacer
                self.rect.y = self.y           #coordonnees du joueur prennent les valeurs d avant la collision

    def reset_pos(self):
        self.rect.x = self.x_initial
        self.rect.y = self.y_initial
        self.x = self.x_initial
        self.y = self.y_initial
        self.image = self.imagearrière

    def ouvrir_porte(self):
        porte_colliddé= pygame.sprite.spritecollide(self, self.jeu.liste_portes,False)
        if porte_colliddé:
            for obj_pris in self.jeu.objet_pris_liste:
                if obj_pris.name == porte_colliddé[0].cle:
                    porte_colliddé[0].remove(self.jeu.tout_sprites)
                    porte_colliddé[0].remove(self.jeu.obstacles_sprites)
                    self.ancienne_porte = porte_colliddé[0]
        else:
            if self.ancienne_porte != 0:
                self.ancienne_porte.add(self.jeu.tout_sprites)

    def acide(self):
        if 510<self.rect.x<550 and 2000<self.rect.y< 2200:
            for item in self.jeu.objet_pris_liste:
                if item.name == "soda":
                    self.jeu.acide.add(self.jeu.objet_pris_liste)
                    self.jeu.soda.remove(self.jeu.objet_pris_liste)


    def machine_vendeuse(self):

        if 2240<self.rect.left<2370 and  1585<self.rect.y<1602:
            for item in self.jeu.objet_pris_liste:
                if item.name == "piece":
                    self.jeu.piece.remove(self.jeu.objet_pris_liste)
                    self.jeu.soda.add(self.jeu.objet_pris_liste)

    def update(self):
        self.mouvement()


        if self.vel_x != 0 and self.vel_y != 0:
            self.vel_x = self.vel_x * 0.71
            self.vel_y = self.vel_y * 0.71  # racine carré de 2
        self.x += self.vel_x
        self.y += self.vel_y  # Update valor fantasma
        self.rect.x = self.x
        self.ouvrir_porte()
        self.collision('x')
        self.rect.y = self.y
        self.ouvrir_porte()
        self.collision('y')
        self.machine_vendeuse()




        # update valor fantasma valor real


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, jeu, x, y, largeur, hauteur, ):
        self.group = jeu.obstacles_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.rect.x = x
        self.rect.y = y
        self.jeu = jeu

class Objet_P (pygame.sprite.Sprite):

    def __init__(self, jeu,visible,image, nom, x, y):
        if visible == True:
            self.groupe = jeu.objet_p, jeu.tout_sprites
        else:
            self.groupe = jeu.objet_p
        pygame.sprite.Sprite.__init__(self, self.groupe)
        self.image = pygame.image.load(image)
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.rect.y = y
        self.inventaire_x = 0
        self.inventaire_y= 0
        self.pris = False
        self.name = nom
        self.jeu = jeu
        self.son = pygame.mixer.Sound("cle_test.wav")   #son de prise objet
        self.channel = pygame.mixer.Channel(0)

    def prendre(self):

        collision = pygame.sprite.collide_rect(self, self.jeu.joueur)

        if collision:
            self.pris= True
            self.remove(self.jeu.tout_sprites)
            self.add(self.jeu.objet_pris_liste)
            self.channel.play(self.son,  maxtime=2000)   #creer des diferentes chaines pour jouer 2 a la fois


    def update(self):
        self.prendre()


            #enlever objet liste_tout_sprites qui est blité

class Porte(pygame.sprite.Sprite):

    def __init__(self, jeu,x, y, image,cle):
        self.jeu= jeu
        self.group= self.jeu.tout_sprites, self.jeu.liste_portes,self.jeu.obstacles_sprites
        pygame.sprite.Sprite.__init__(self, self.group)
        self.image = pygame.image.load(image)
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.rect.y = y
        self.cle = cle


    def dessin_portes(self):
        self.jeu.ecran.blit(self.image, (self.x,self.y))

    def ouvrir(self):

        # if pygame.sprite.spritecollide(self.jeu.joueur, self.jeu.liste_portes,False):
        #     for obj_pris in self.jeu.objet_pris_liste:
        #         if obj_pris.name == self.cle:
        # #             self.remove(self.jeu.tout_sprites)
        #
        #
        # else:
        #     self.add(self.jeu.tout_sprites)

        pass



class Inventaire():


    def __init__(self, jeu, image):
        self.jeu = jeu
        self.image = pygame.image.load(image)
        self.rect = pygame.Surface.get_rect(self.image)#colocar foto inventario
        self.x = 1280 * 1/3
        self.y = 800 - 170

    def objet_montre(self):
        decalage_x=0
        for objet_test in self.jeu.objet_pris_liste:
            self.jeu.ecran.blit(objet_test.image, (self.x+11+(80-objet_test.rect.width)/2+decalage_x,self.y+16+(80-objet_test.rect.width)/2)) #localisation
            decalage_x += 81

    def update(self):
        self.objet_montre()





class Professeur(pygame.sprite.Sprite):
    def __init__(self, game, x, y, imagedevant, imagederriere,personnel):
        pygame.sprite.Sprite.__init__(self,game.tout_sprites)
        self.imagederriere = pygame.image.load(imagederriere)
        self.imagedevant = pygame.image.load(imagedevant)
        self.image = self.imagedevant
        self.rect = pygame.Surface.get_rect(self.image)
        self.x = x
        self.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.rect.x = x
        self.etape = 0
        self.rect.y = y
        self.cf = 0
        self.game = game
        self.chemincalculé = False
        self.test = True
        self.arrivé = False
        self.afficher_bulle = True
        self.personnel = personnel
        if CHECKAGE == True:
            self.checkage = True
        else:
            self.checkage = False



    def mouvement2(self, cordB):

        if self.chemincalculé == False:
            self.chemin = testmouvement(self,cordB)
            self.chemincalculé = True
        prochCord = self.chemin[self.etape]

        if 0 <= (abs(prochCord[0] - self.rect.x)) < 1:
            self.vel_x = 0
        elif prochCord[0] > self.rect.x:
            self.vel_x = 1
        elif prochCord[0] < self.rect.x:
            self.vel_x = -1

        if 0 <= (abs(prochCord[1] - self.rect.y)) < 1:
            self.vel_y = 0
        elif prochCord[1] > self.rect.y:
            self.vel_y = 1
            self.image = self.imagedevant
        elif prochCord[1] < self.rect.y:
            self.vel_y = -1
            self.image = self.imagederriere

        if 0 <= (abs(prochCord[0] - self.rect.x)) < 1 and 0 <= (abs(prochCord[1] - self.rect.y)) < 1:
            if self.etape + 1 < len(self.chemin):
                self.etape += 1
            else:
                self.arrivé = not self.arrivé
                self.chemincalculé = not self.chemincalculé
                self.etape = 0





    def check_eleve_endehors_chaise(self):
        if self.game.mode == "cours":
            for chaise_surface in self.game.images_chaises:
                if ((chaise_surface.x-14<=self.game.joueur.rect.x<=(chaise_surface.x+chaise_surface.largeur+14))and(chaise_surface.y<=self.game.joueur.rect.y<=(chaise_surface.y+chaise_surface.hauteur))):
                    return

            self.game.avertissements +=1
            print("avertissements:",self.game.avertissements)








    def collision(self, direction):

        if direction == 'x':
            collision = pygame.sprite.spritecollide(self, self.game.obstacles_sprites, False)
            if collision:  # test de collision
                self.rect.x -= self.vel_x

                # self.x -= self.vel_x
                self.vel_x = 0

        if direction == 'y':
            collision = pygame.sprite.spritecollide(self, self.game.obstacles_sprites, False)
            if collision:  # teste de   xcollisao valores fantasma
                self.rect.y -= self.vel_y

                # self.y -= self.vel_y
                self.vel_y = 0

    def check_eleve_bibliotheque(self):

        if 768<self.game.joueur.rect.x<(962-self.game.joueur.rect.width) and   2430<self.game.joueur.rect.y<2498:
            self.game.avertissements +=1






    def update(self):

        if self.personnel == "professeur":
            horloge = int(pygame.time.get_ticks() / 1000) - self.cf
            if self.game.mode == "recree":
                self.mouvement2((280,1027))
                self.image = self.imagedevant
            if self.game.mode == "cours" or self.game.mode =="cours2":
                if self.image == self.imagedevant and self.checkage == True:
                    self.check_eleve_endehors_chaise()
                if self.arrivé == False and 10 <= horloge <= 25:
                    self.mouvement2((self.x + 64 , self.y - 64))
                elif self.arrivé == True and horloge > 25:
                    self.mouvement2((self.x, self.y))
                elif horloge > 35:
                    self.cf += 35
            if self.game.mode == "cours2" and CHECKAGE == True:
                horloge2 = int(pygame.time.get_ticks()/1000)

                self.checkage = False
                if horloge2 > 300:
                    self.checkage = True

        if self.personnel == "documentariste":
            if self.image == self.imagedevant:
                self.check_eleve_bibliotheque()
            temps = pygame.time.get_ticks()/1000 - self.cf
            if self.arrivé == False and 10 <= temps <= 14:
                self.mouvement2((self.x +10, self.y - 50))
            elif self.arrivé == True and temps > 14:
                self.mouvement2((self.x, self.y))
            elif temps > 25:
                self.cf += 25




        # self.mouvement((1324, 2200))
        self.rect.x += self.vel_x
        self.collision('x')
        self.rect.y += self.vel_y
        self.collision('y')



class Bulle(pygame.sprite.Sprite):

    def __init__(self,jeu,sprite,texte):
        self.groupe = jeu.liste_bulles
        pygame.sprite.Sprite.__init__(self,self.groupe)
        self.sprite = sprite
        self.texte = texte
        self.font = pygame.font.Font("Letters for Learners.ttf",15)
        self.image = pygame.image.load("bule_parole.png")
        self.rect = pygame.Surface.get_rect(self.image)
        self.montrer_bulle = False
        self.jeu = jeu
        self.cf= 0
        self.x = 0


    def parole_dessin(self):
        self.parole = self.font.render(self.texte, True, (0, 0, 0))
        self.parole_rect = pygame.Surface.get_rect(self.parole)
        self.parole_rect.x = self.rect.x + 10
        self.parole_rect.y = self.rect.y + 4


    def update(self):
        self.rect.x = self.sprite.rect.x+self.sprite.rect.width/2+5
        self.rect.y = self.sprite.rect.y-self.sprite.rect.height/2-3
        self.parole_dessin()
        if self.sprite.afficher_bulle ==True:
            temps = pygame.time.get_ticks()/1000-self.cf
            co = randint(-5,5)
            if temps+co>25:
                self.montrer_bulle = True
            if temps>30:
                self.montrer_bulle = False
                self.cf += 30

    def dessin_bulle(self):


        if self.sprite.afficher_bulle == True and self.montrer_bulle == True:
            self.jeu.ecran.blit(self.image, self.jeu.camera.translation(self))
            self.jeu.ecran.blit(self.parole, self.jeu.camera.translation_rect(self.parole_rect))








class Eleve(pygame.sprite.Sprite):

    def __init__(self,jeu, x,y):

        self.groupe= jeu.tout_sprites, jeu.liste_eleves
        pygame.sprite.Sprite.__init__(self,self.groupe)
        self.coord_chaise = (x,y)
        self.game = jeu
        NumImage = randint(1,3)
        self.imagedevant = pygame.image.load("eleve_devant_{0}.png".format(NumImage))
        self.imagederriere = pygame.image.load("eleve_derriere_{0}.png".format(NumImage))
        self.image = self.imagederriere
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.x = x
        self.y = y
        self.rect.y = y
        self.chemincalculé = False
        self.etape = 0
        self.vel_x = 0
        self.vel_y = 0
        self.arrivé = False
        self.arrivé_recree = False
        self.cf = randint(-100,100)
        self.cf2 = randint(-200,200)
        self.deltat = 0

    def mouvement2(self, cordB):

        if self.chemincalculé == False:
            self.chemin = testmouvement(self,cordB)
            self.chemincalculé = True
        prochCord = self.chemin[self.etape]

        if 0 <= (abs(prochCord[0] - self.rect.x)) < 1:
            self.vel_x = 0
        elif prochCord[0] > self.rect.x:
            self.vel_x = 1
        elif prochCord[0] < self.rect.x:
            self.vel_x = -1

        if 0 <= (abs(prochCord[1] - self.rect.y)) < 1:
            self.vel_y = 0
        elif prochCord[1] > self.rect.y:
            self.vel_y = 1
            self.image = self.imagedevant
        elif prochCord[1] < self.rect.y:
            self.vel_y = -1
            self.image = self.imagederriere

        if 0 <= (abs(prochCord[0] - self.rect.x)) < 1 and 0 <= (abs(prochCord[1] - self.rect.y)) < 1:
            if self.etape + 1 < len(self.chemin):
                self.etape += 1
            else:
                self.arrivé = not self.arrivé
                self.chemincalculé = not self.chemincalculé
                self.etape = 0




    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.game.mode == "recree":
            if self.arrivé == False and self.arrivé_recree == False:
                self.mouvement2((1059, 1490))
            if self.arrivé == True and self.arrivé_recree == False:
                self.arrivé_recree = True
                self.arrivé = False
            if self.arrivé_recree == True:

                self.mouvement2((1400 + self.cf, 1500 + self.cf2))
            if self.arrivé_recree and self.arrivé:
                self.mouvement2((1400 - self.cf, 1500 - self.cf2))

        if self.game.mode == "cours2":
            self.mouvement2((self.x, self.y))
            if self.arrivé:
                self.image = self.imagederriere

            #Ce que l'éleve fait pour aller et pendant le cours de sport
            #self.mouvement2((coord))
            #self.arrivé_sport_




class Horloge():
    def __init__(self, game):
        self.cf = 0
        self.images = {}
        for i in range(10):
            self.images["image{0}".format(i)] = pygame.image.load("numero{0} copy.png".format(i))
        self.minutes = 0
        self.heures = 8
        self.tempsdujeumin = 0
        self.game = game

    def compteur(self):
        temps = int(pygame.time.get_ticks() / 1000) - self.cf
        if temps > CFTEMPS:
            self.cf += CFTEMPS
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.heures += 1

    def imagessurface(self):
        if len(str(self.minutes)) == 1:
            numéromin2 = 0
            numéromin1 = str(self.minutes)[0]
        else:
            numéromin2 = str(self.minutes)[0]
            numéromin1 = str(self.minutes)[1]
        if len(str(self.heures)) == 1:
            numérohr1 = str(self.heures)[0]
            numérohr2 = 0
        else:
            numérohr1 = str(self.heures)[1]
            numérohr2 = str(self.heures)[0]
        self.game.ecran.blit(self.images["image{0}".format(numéromin1)], (330, 10))  # on affiche le premier numéro
        self.game.ecran.blit(self.images["image{0}".format(numéromin2)], (230, 10))
        self.game.ecran.blit(self.images["image{0}".format(numérohr1)], (110, 10))

        self.game.ecran.blit(self.images["image{0}".format(numérohr2)], (10, 10))

    def update(self):
        self.compteur()
        self.tempsdujeumin = self.heures * 60 + self.minutes


class Chaise(pygame.sprite.Sprite):

    def __init__(self,jeu,x,y,largeur,hauteur):
        self.groupes = jeu.images_chaises
        pygame.sprite.Sprite.__init__(self,self.groupes)
        self.image = pygame.image.load("chaise_partie_trans.png")
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x +18
        self.rect.y = y +48
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur


class Affiche(pygame.sprite.Sprite):

    def __init__(self,jeu, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image_affiche.png")
        self.rect = pygame.Surface.get_rect(self.image)
        self.rect.x = x
        self.rect.y = y
        self.dessiner_affiche = True
        self.jeu = jeu


    def entree_utilisateur(self):
        boutton = pygame.mouse.get_pressed()
        position_mouse = pygame.mouse.get_pos()
        if boutton[0] ==1 and (self.rect.x<position_mouse[0]<(self.rect.x +self.rect.width)) and (self.rect.y<position_mouse[1]<(self.rect.y+self.rect.height)):
            self.dessiner_affiche= False

    def dessin(self):
        if self.dessiner_affiche == False:
            pass
        else:
            self.jeu.ecran.blit(self.image, (self.rect.x,self.rect.y))



class Camera:
    def __init__(self, Hauteur, Largeur):
        self.camerarectangle = pygame.Rect(0, 0, Hauteur, Largeur)
        self.Hauteur = Hauteur
        self.Largeur = Largeur

    def translation(self, entite):
        return entite.rect.move(self.camerarectangle.topleft)

    def translation_rect(self,rectangle):
        return rectangle.move(self.camerarectangle.topleft)

    def update(self, cible):
        x = -cible.rect.centerx + int(LARGEUR / 2)
        y = -cible.rect.centery + int(HAUTEUR / 2)
        x = min(0, x)
        y = min(0, y)

        self.camerarectangle = pygame.Rect(x, y, self.Hauteur, self.Largeur)

class Espace():

    def __init__(self, nom_espace,x,y,hauteur,largeur):
        self.nom = nom_espace
        self.x = x
        self.y = y
        self.hauteur = hauteur
        self.largeur = largeur

class Fond:
    def __init__(self):
        self.image = pygame.image.load("Phase1.png")
        self.rect = pygame.Surface.get_rect(self.image)
        self.carte_tmx = pytmx.load_pygame("Phase1.tmx")

    def render(self, surface):
        for layer in self.carte_tmx.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.carte_tmx.get_tile_image_by_gid(gid)
                    if tile:
                        surface.blit(tile, (x * self.carte_tmx.tilewidth, y * self.carte_tmx.tileheight))

    def fondsurf(self):
        surface2 = pygame.Surface(
            (self.carte_tmx.width * self.carte_tmx.tilewidth, self.carte_tmx.height * self.carte_tmx.tileheight))
        self.render(surface2)

        return surface2
