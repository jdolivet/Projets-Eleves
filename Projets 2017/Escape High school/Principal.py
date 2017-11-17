import pygame
import sys
from Reglages import *
from classes import *
import pytmx


class jeu:

    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))    ##initialisation du jeu
        pygame.display.set_caption(TITREAFFICHAGE)
        self.clock = pygame.time.Clock()
        self.fond = Fond()
        self.carte= pytmx.load_pygame("Phase1.tmx")
        self.fond_img = self.fond.fondsurf()
        self.fond_rect = pygame.Surface.get_rect(self.fond_img)
        self.horlogera = Horloge(self)



    def load_data(self):  #importer images
        pass

    def nouveau(self): #setup nouveau jeu

        self.obstacles_sprites = pygame.sprite.Group()
        self.tout_sprites = pygame.sprite.Group()       #Création de groupes de Sprites
        self.liste_avec_joueur = pygame.sprite.Group()
        self.liste_eleves = pygame.sprite.Group()
        self.liste_portes = pygame.sprite.Group()
        self.images_chaises = pygame.sprite.Group()
        self.npc_sprites = pygame.sprite.Group()#creation groupes de sprites
        self.inventairedejeu = Inventaire(self, "inventaire.png")
        self.objet_p = pygame.sprite.Group()
        self.objet_pris_liste= pygame.sprite.Group()
        self.liste_bulles = pygame.sprite.Group()

        for objets in self.carte.objects:                           # Itération par  les "objets dans le documents Phase1.tmx de l'éditeur Tiled Map
            if objets.name == "mur":
                Obstacle(self,objets.x, objets.y, objets.width,objets.height)  #Création d'objets en fonction des objets rencontrés
            if objets.name == "obstacle":
                Obstacle(self,objets.x, objets.y, objets.width,objets.height)
            if objets.name == "porte":
                Porte(self, objets.x, objets.y, "porte_rouge.png",objets.properties["cle"])
            if objets.name == "chaise":
                Chaise(self,objets.x, objets.y,objets.width,objets.height)
            if objets.name == "machine_vendeuse":
                self.machine_vendeuse = pygame.Rect(objets.x,objets.y,objets.width, objets.height)


        self.joueur = Joueur(self,530,1430)            #Création Objet Joueur

        self.eleve1 = Eleve(self,530,1240)
        self.eleve2 = Eleve(self,400,1430)
        self.eleve3 = Eleve(self,268,1427)

        self.cle_labo = Objet_P(self,True, "cles.png", "cle_labo",256 ,1086 )
        self.piece = Objet_P(self,True, "piece.png", "piece",790, 2490 )
        self.professeur = Professeur(self,470,1100,"professeur_devant.png","professeur_derriere.png","professeur")
        self.documentariste = Professeur(self,850,2433,"documentariste_devant.png","documentariste_derriere.png","documentariste")
        self.soda = Objet_P(self,False, "soda.png", "soda",0,0)
        self.acide = Objet_P(self, False, "acide.png", "acide", 0,0)

        self.bulle_professeur = Bulle(self, self.professeur, "8 bits = 1 octet")
        self.affiche_début = Affiche(self, 800,50)


        self.camera = Camera(LARGEUR, HAUTEUR)

        self.cf=0
        self.minutes = 0
        self.avertissements = 0
        self.delta_avertissement =0




    def loop_jeu(self):
        self.jouant = True

        while self.jouant:
            self.clock.tick(FPS)
            self.evenements()
            self.emploiedutemps()
            self.update()
            self.dessin()



    def evenements(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.sortie()
        self.affiche_début.entree_utilisateur()

    def emploiedutemps(self):
        if (self.horlogera.heures)==8:
            self.mode="cours"
        elif self.horlogera.heures==10 :
            self.mode= "recree"
        elif self.horlogera.heures == 13:
            self.mode = "cours2"
        elif self.horlogera.heures == 15:
            self.mode = "recree"
        elif self.horlogera.heures == 16:
            self.sortie()
        print(self.mode)

    def sortie(self):

        pygame.quit()
        sys.exit()

    def update(self):
        self.horlogera.update()
        if self.avertissements - self.delta_avertissement == 1:
            self.joueur.reset_pos()
        self.bulle_professeur.update()

        self.delta_avertissement = self.avertissements
        for porte_sprite in self.liste_portes:
            porte_sprite.ouvrir()
        self.tout_sprites.update()
        self.eleve1.update()
        self.camera.update(self.joueur)
        if self.avertissements > 3:
            self.sortie()





    def dessin(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.ecran.blit(self.fond_img, self.camera.translation(self.fond))
        for sprite in self.tout_sprites:
            self.ecran.blit(sprite.image, self.camera.translation(sprite))

        #self.tout_sprites.draw()
        for chaise_sprite in self.images_chaises:
            self.ecran.blit(chaise_sprite.image, self.camera.translation(chaise_sprite))
        for bulles in self.liste_bulles:
            bulles.dessin_bulle()
        self.affiche_début.dessin()
        self.horlogera.imagessurface()
        self.ecran.blit(self.inventairedejeu.image, (self.inventairedejeu.x, self.inventairedejeu.y))
        self.inventairedejeu.objet_montre()
        pygame.display.flip()

nossojeu = jeu()

while True:
    pygame.mixer.music.load("music_fond.wav")   #load la musique en fichier wav
    pygame.mixer.music.play(-1)   #joue musique infinitement
    pygame.mixer.music.set_volume(0.1)  #regle hauteur de la musique

    nossojeu.nouveau()
    nossojeu.loop_jeu()

