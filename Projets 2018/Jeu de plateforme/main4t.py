import pygame as pg
import sys
from os import path
from settings2t import *
from sprite3t import *
from tilemap2t import *

def Quit():
    pg.quit()
    sys.exit()
def events():
        # evenements du jeu (quiter)
    for event in pg.event.get():
          
        if event.type==pg.QUIT:
            Quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Quit()

def jogo():
#INITIALISATION DU JEU
    pg.init() # INITIALISATION DE PYGAME
    pg.mixer.init() # INITIALISATION DU SISTEME AUDIO
    pg.mixer.music.load('FromHere.ogg') # CHARGEMENT ET RÉGLAGE DE LA MUSIQUE
    pg.mixer.music.set_volume(0.2)#AJUSTE VOLUME
    pg.mixer.music.play(-1)
    screen = pg.display.set_mode((LARGEUR, HAUTEUR))#CREE LA FENETRE DU JEU
    pg.display.set_caption(TITRE)#AFFICHE LE TITRE
    clock = pg.time.Clock()#INITIALISE L'HORLOGE
  
    game_folder = path.dirname(__file__)
    img_folder = path.join(game_folder,'img')#PREND DE L'ORDINATEUR LE DOSSIER img ou il ya toutes les images
    map_folder = path.join(game_folder,'maps')#PREND DE L'ORDINATEUR LE DOSSIER maps ou il y a la map du jeu

    Map = TiledMap(path.join(map_folder,'tiledk.tmx'))#CREE LA MAP DU JEU
    map_img =Map.make_map()## CREE LA SURFACE DU JEU
    map_rect = map_img.get_rect()##CREE UN RECTANGLE POUR LA SURFACE DU JEU
    camera = Camera(Map.width, Map.height)#CREE LA CAMERA POUR NOTRE MAP
    print(Map.width, Map.height)

    playing = True       
    dt=clock.tick(FPS)/30.#TEMPS D'UNE BOUCLE

  
    player=Player(100, 1700)


#######BOUCLE DU JEU###
            

    while playing:
        pg.time.delay(int(dt))##BOUCLE DURE LE MEME TEMPS
        events()
        playing=player.update()###TOUT LES BOUCLES ON FAIT UPDATE DU PLAYER et LA FIN DE LA BOUCLE DEPEND DE CETTE UPDATE
        camera.update(player)#UPDATE DE LA CAMERA POUR LE PLAYER
        vie1.update()
        vie2.update()
        vie3.update()
        life=player.Nb_vie##NOMBRE DE VIES DU PLAYER
        vie1.afficher(life)
        ###UPDATE DES ENEMIS######
        enemy_group1.update()

        x=player.pos[0]##POSITION DU PLAYERx
        y=player.pos[1]##POSITION DU PLAYERy
        enemy_group2.update(x,y)##UPDATE DE L'ENEMI QUI SUIT LE PLAYER
###########UPDATE DE LA VIE ET AFFICHAGE DE SON IMAGE
        vie1.update()
        vie2.update()
        vie3.update()
        life=player.Nb_vie##NOMBRE DE VIE DU PLAYER
########AFFICHAGE DU PLAYER DE LA MAP ET DES ENNEMIS
        screen.blit(map_img, camera.apply_rect(map_rect))
        screen.blit(player.image, camera.apply(player))#surface image player, rectangle du player deplacer par combien camera 
        vie1.afficher(life)##AFICHE IMAGE VIE
        screen.blit(enemy1.image, camera.apply(enemy1))
        screen.blit(enemy2.image, camera.apply(enemy2))
        screen.blit(enemya.image, camera.apply(enemya))

        pg.display.flip()
            

 ###FONCTION DU MENU           
def menu():
    pg.init()
    clock = pg.time.Clock()
    pas_cliquer = True
    while pas_cliquer:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        screen.fill(BLANC)##REMPLI LA FENETRE EN BLANC
        grand_texte= pg.font.Font('freesansbold.ttf',30)               
        TexteSurf , TexteRect = texte_objets('Pour commencer le jeu, appuyez sur x', grand_texte) 
        TexteRect.center = ((LARGEUR/2),(HAUTEUR/2)) ##CENTRE LE TEXT
        screen.blit(TexteSurf,TexteRect) #AFFICHE LE TEXT
        pg.display.update()
        keys = pg.key.get_pressed()
        if keys[pg.K_x]:
            pas_cliquer = False
    jogo()
    menu()


menu()





