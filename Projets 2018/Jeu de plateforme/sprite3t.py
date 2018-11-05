from os import path
import pygame as pg
from random import uniform
from settings2t import *
from tilemap2t import *

import time
import sys

##TEMPS D'UNE BOUCLE
clock = pg.time.Clock()
dt=clock.tick(FPS)/30 #TEMPS D'UNE BOUCLE

##GESTION DES SONS
pg.init()
pg.mixer.init()
son_cri = pg.mixer.Sound('cri.wav')
son_gagne = pg.mixer.Sound('gagne.wav')
son_saut = pg.mixer.Sound('saut.wav')

#### QUITTE LE JEU
def Quit():
    pg.quit()
    sys.exit()


def events():
    # EVENEMENT QUITTER
    for event in pg.event.get():
          
        if event.type==pg.QUIT:
            Quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                Quit()


###FONCTIONS POUR AJUSTER LA POSITION LORS DE LA COLLISION

###FONCTION QUI RETOURNELE RECTANGLE DE COLLISION DU JOUEUR
def collide_hit_rect(sprite1, sprite2):
    return sprite1.hit_rect.colliderect(sprite2.rect)
def collide(sprite, group, dir):
    
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False,collide_hit_rect) 
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx: #deplace ver la droite 
                sprite.pos[0] = hits[0].rect.left - sprite.hit_rect.width / 2 - 3
            if hits[0].rect.centerx < sprite.hit_rect.centerx: #deplace vers la gauche
                sprite.pos[0] = hits[0].rect.right + sprite.hit_rect.width / 2 + 3 
            sprite.hit_rect.centerx = sprite.pos[0]
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group,  False,collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery: #deplace ver le haut
                sprite.pos[1] = hits[0].rect.top - sprite.hit_rect.height / 2

            if hits[0].rect.centery < sprite.hit_rect.centery: #deplace vers le bas
                sprite.pos[1] = hits[0].rect.bottom + sprite.hit_rect.height / 2 + 3
            sprite.Vy = 0
            sprite.hit_rect.centery = sprite.pos[1]


###CLASSE DE LA ZONE DE L OBJECTIF FINAL 
class GO(pg.sprite.Sprite):
     def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y

#CLASSE DE L'OBSTACLE AU FOND DU TROU
class Death(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y
###CLASSE DES PLATFORM
class Obstacle(pg.sprite.Sprite):
   def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y 
###CLASSE POUR LE CHECKPOINT POUR LE PLAYER
class Checkpoint(pg.sprite.Sprite):
   def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.rect = pg.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.rect.x = x 
        self.rect.y = y 


screen = pg.display.set_mode((LARGEUR, HAUTEUR)) #ECRAN

#CREATION DE GROUPE DE SPRITES
death = pg.sprite.Group()
obstacle = pg.sprite.Group()
go = pg.sprite.Group()
checkpoint = pg.sprite.Group()

game_folder = path.dirname(__file__)
map_folder = path.join(game_folder,'maps')
Map = TiledMap(path.join(map_folder,'tiledk.tmx'))

###LIT LA MAP, DONNE LES CORDONEES POUR LES CLASSES VUES CI-DESSUS ET LES AJOUTE DANS LEURS GROUPES RESPECTIFS
for tile_object in Map.tmxdata.objects:
           
    if tile_object.name =="platform":
        obstacle1=Obstacle(tile_object.x,tile_object.y,tile_object.width,tile_object.height)
        obstacle.add(obstacle1)
    if tile_object.name =="death":
        death1=Death(tile_object.x,tile_object.y,tile_object.width,tile_object.height)
        death.add(death1)
    if tile_object.name =="go":
        go1=GO(tile_object.x,tile_object.y,tile_object.width,tile_object.height)
        go.add(go1)
    if tile_object.name =="checkpoint":
        check1=Checkpoint(tile_object.x,tile_object.y,tile_object.width,tile_object.height)
        checkpoint.add(check1)
        
##AFFECTATION DES 5 COORDONEES DE CHECKPOINT   
for i in checkpoint:
    posit=i.x
    if posit<460:
        p1=posit
    if posit<1210 and posit>460:
        p2=posit
    if posit<1760 and posit>1210:
        p3=posit    
    if posit<2360 and posit>1790:
        p4=posit
    if posit<2945 and posit>2360:
        p5=posit



####FONCTION POUR AFFICHER UN MESSAGE

def texte_objets(texte,police): #sert à créer le rectangle et la surface de l'image
    surfaceT = police.render(texte, True, NOIR)
    return surfaceT, surfaceT.get_rect()    
def message(texte):
    clock = pg.time.Clock()
 
    grand_texte= pg.font.Font('freesansbold.ttf',40)
    TexteSurf , TexteRect = texte_objets(texte, grand_texte)
    TexteRect.center = ((LARGEUR/2),(HAUTEUR/2))
    screen.blit(TexteSurf,TexteRect)
    pg.display.update()
    time.sleep(1)
 
            
###AFFICHE MESSAGE LORS DE LA MORT DU PLAYER OU QUAND IL A PERDU UNE VIE
def morte():
    message("Vous avez perdu une vie")

def gameover():
    message("Vous avez perdu! N pour rejouer et X pour quitter")
    toucher= True
    keys = pg.key.get_pressed()
    while toucher:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        if keys[pg.K_n]:
            toucher= False
        if keys[pg.K_x]:
            pg.quit()
            sys.quit()

####MESSAGE POUR RECOMMENCER OU QUITER APRES AVOIR GAGNE      
def gagner():
    message("Vous avez réussi! N pour rejouer et X pour quitter")
    toucher= True
    keys = pg.key.get_pressed()
    while toucher:
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                
        if keys[pg.K_n]:
            toucher= False
        if keys[pg.K_x]:
            pg.quit()
            sys.quit()

####VIE DU PLAYER
class Vie(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        vie_img = pg.image.load(path.join(img_folder,VIE_IMG )).convert_alpha()
        self.image = vie_img
        self.rect = self.image.get_rect()#Fetch the rectangle object that has the dimensions of the image
        self.pos = [x, y]         

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
####AFFICHAGE DE L'IMAGE DE LA VIE EN FONCTION DU NB de VIE DU PLAYER
    def afficher(self,life):
        if life==3:
            screen.blit(self.image,vie1.rect)
            screen.blit(self.image,vie2.rect)
            screen.blit(self.image,vie3.rect)
            
        elif life==2:
            screen.blit(self.image,vie1.rect)
            screen.blit(self.image,vie2.rect)
        elif life==1:
            screen.blit(self.image,vie1.rect)
      

##CREE 3 IMAGES DE VIES ET ON DEFINI LEUR POSITION DANS LA MAP
vie1=Vie(920,70) 
vie2=Vie(870,70)
vie3=Vie(820,70)




###ENNEMIS
class Ennemi(pg.sprite.Sprite):
    
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        enemy_img = pg.image.load(path.join(img_folder,ENNEMY_IMG )).convert_alpha()
        self.image = enemy_img
        self.image = pg.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect() #Prend le rectangle qui a les dimensions de l'image
        
        self.Vy=5*dt #vitesse vertical
        self.VHor = 4*dt #vitesse horizontal
        self.pos = [x, y] 
      
    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #MET LA POSITION DANS LE CENTRE DU RECTZNGLE DE L ENNEMI
        hits = pg.sprite.spritecollide(self, obstacle, False)
        if hits:
            self.pos[0] += self.VHor 
            cote_droite=hits[0].rect.right-21
            cote_gauche=hits[0].rect.left+21
            if self.pos[0]>cote_droite or self.pos[0]<cote_gauche:
                self.VHor=-self.VHor
        if not hits:           
            self.pos[1] += self.Vy
            self.Vy += gravite
    

class Ennemi1(pg.sprite.Sprite):
    
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder,'img')
        enemy_img = pg.image.load(path.join(img_folder,ENNEMY_IMG )).convert_alpha()#AFFECTE POUR L'ENNEMI SA PHOTO
        self.image = enemy_img
        self.image = pg.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect() #Fetch the rectangle object that has the dimensions of the image
        
        self.Vy= 4*dt #vitesse vertical
        self.VHor = 4*dt #vitesse horizontal
        self.pos = [x, y] 
      
    def update(self,posplayerx,posplayery):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        hits = pg.sprite.spritecollide(self, obstacle, False)
        distancex= abs(self.pos[0]-posplayerx)
        distancey= abs(self.pos[1]-posplayery)
        self.Vy=int(self.Vy)
        self.VHor=int(self.VHor)
        if self.pos[0]>posplayerx:
            self.pos[0]= self.pos[0] - self.VHor
            
        elif self.pos[0]<posplayerx:
            self.pos[0]= self.pos[0] + self.VHor
            
        if self.pos[1]>posplayery + (self.Vy-0.5):
            self.pos[1]= self.pos[1] - self.Vy           
        elif self.pos[1]<posplayery:
            self.pos[1]= self.pos[1] + self.Vy
        

enemya=Ennemi1(850,2050) #CREE ENNEMI DANS LA POSITION DESIREE
enemy_group2=pg.sprite.Group()
enemy_group2.add(enemya) #ON AJOUTE LES ENNEMIS QUI SUIT LE PLAYER DANS UN GROUP

enemy1=Ennemi(300,2000) 
enemy2=Ennemi(1975,1930)
enemy_group1 = pg.sprite.Group()
enemy_group1.add(enemy1)
enemy_group1.add(enemy2)



####CLASS DO PLAYER#############
class Player(pg.sprite.Sprite):
    
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        game_folder = path.dirname(__file__)
        #######GESTION IMAGES
        img_folder = path.join(game_folder,'img')
        self.player_img = pg.image.load(path.join(img_folder, IMOBILE_IMG)).convert_alpha() #Crée la surface de la photo 
        self.player_img = pg.transform.scale(self.player_img,(32,32))
        ### IMAGES POUR L'ANIMATION
        self.avant1_img = pg.image.load(path.join(img_folder, MARCHE_AVANT1)).convert_alpha()
        self.avant1_img = pg.transform.scale(self.avant1_img,(32,32))
        self.avant2_img = pg.image.load(path.join(img_folder, MARCHE_AVANT2)).convert_alpha()
        self.avant2_img = pg.transform.scale(self.avant2_img, (32, 32))
        self.avant3_img = pg.image.load(path.join(img_folder, MARCHE_AVANT3)).convert_alpha()
        self.avant3_img = pg.transform.scale(self.avant3_img, (32, 32))
        self.saute_img = pg.image.load(path.join(img_folder, SAUTE_IMG)).convert_alpha()
        self.saute_img = pg.transform.scale(self.saute_img, (32, 32))
        self.saute2_img = pg.transform.flip(self.saute_img,True,False)
        self.saute2_img = pg.transform.scale(self.saute2_img, (32, 32))
        self.player2_img = pg.transform.flip(self.player_img,True,False) ### Le second argument est une inversion selon l'axe x et le troisieme c'est une selon l'axe y
        self.arriere1_img = pg.transform.flip(self.avant1_img,True,False)
        self.arriere2_img = pg.transform.flip(self.avant2_img,True,False)
        self.arriere3_img = pg.transform.flip(self.avant3_img,True,False)
        ###LISTE IMAGE POUR ANIMATION
        self.LISTE2_IMG = [self.player2_img,self.arriere1_img,self.arriere2_img,self.arriere3_img]
        self.LISTE_IMG = [self.player_img, self.avant1_img, self.avant2_img, self.avant3_img]
        self.compteur1_liste_img = 0
        self.compteur2_liste_img = 0
        self.image = self.player_img
        self.rect = self.image.get_rect() #Prend le rectangle qui a les dimensions de l'image
        self.height=self.rect.height
        self.width=self.rect.width

        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        
        self.VHor = 10 #vitesse horizontale
        self.Vy= 0 #vitesse verticale
        self.Vsalto = 25 #vitesse du saut
        self.pos = [x, y] 
        obstacle = pg.sprite.Group()
        self.Nb_vie=3
        self.X1=0
        
#####Fonction pour sauter
    def saute(self):
        hits = pg.sprite.spritecollide(self, obstacle, False)
        if hits:
            self.Vy = 0
            self.Vy-= self.Vsalto
            
    ######Fonction pour aller a droite gauche et sauter
    def get_keys(self): 
        keys = pg.key.get_pressed()
        #variables utiles pour l'animation
        global marche_avant #permet de savoir si le joueur marche à droite
        marche_avant = False 
        global marche_arriere #permet de savoir si le joueur marche à gauche
        marche_arriere = False
        if keys[pg.K_LEFT] or keys[pg.K_q]: #Pour marcher à gauche 
            self.pos[0] -= self.VHor
            marche_arriere = True
        if keys[pg.K_RIGHT] or keys[pg.K_d]: #Pour marcher à droite 
            self.pos[0] += self.VHor
            marche_avant = True
        if keys[pg.K_UP] or keys[pg.K_SPACE]: #Pour sauter
            son_saut.play()
            self.saute()
    
        
  
    def update(self):
        
        self.get_keys()
        keys = pg.key.get_pressed()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos #ajuste le centre de l'image avec le centre du rectangle du joueur
        self.centery = self.pos[1]
        self.centerx = self.pos[0]

###AJUSTER POSITIONS LORS DE COLLIDE
        self.hit_rect.centerx = self.pos[0]
        collide(self, obstacle, 'x')
        self.hit_rect.centery = self.pos[1]
        collide(self, obstacle, 'y')
        self.rect.center = self.hit_rect.center





##### ANIMATION POUR MARCHER AVANT
 
        hits = pg.sprite.spritecollide(self, obstacle, False)
        if marche_avant == True:
            self.compteur1_liste_img += 1
            i = self.compteur1_liste_img % 4
            self.image = self.LISTE_IMG[i]
            
##### ANIMATION POUR MARCHER ARRIERE     
        
        if marche_arriere == True:
            self.compteur2_liste_img += 1
            k = self.compteur2_liste_img % 4
            self.image = self.LISTE2_IMG[k]
                       
            
###GRAVITE ET IMAGE EN AIR

        if not hits or keys[pg.K_SPACE] or keys[pg.K_UP]:

            self.pos[1] += self.Vy*dt
            if self.Vy < 25:
                self.Vy += gravite
            
            if marche_avant:
                self.image = self.saute_img
            if marche_arriere:
                self.image = self.saute2_img
            if self.image == self.player2_img:
                self.image = self.saute2_img
            if self.image == self.player_img:
                self.image = self.saute_img
            
#####IMAGE QUAND LE PLAYER NE BOUGE PAS

        if not marche_arriere and not marche_avant and hits:
            if self.image == self.player2_img or self.image == self.arriere1_img or self.image == self.arriere2_img or self.image == self.arriere3_img:
                self.image = self.player2_img
            if self.image == self.player_img or self.image == self.avant1_img or self.image == self.avant2_img or self.image == self.avant3_img:
                self.image = self.player_img
            if self.image == self.saute_img:
                self.image = self.player_img
            if self.image == self.saute2_img:
                self.image = self.player2_img
            
 
#####CHECKPOINT
        hits4 = pg.sprite.spritecollide(self, checkpoint, False)
        if self.pos[0]>p1:
            self.X1=p1
        if self.pos[0]>p2:
            self.X1=p2
        if self.pos[0]>p3:
            self.X1=p3
        if self.pos[0]>p4:
            self.X1=p4
        if self.pos[0]>p5:
            self.X1=p5


#######COLLIDE COM ENNEMY###
        hits5=pg.sprite.spritecollide(self,enemy_group1,False)
        hits6=pg.sprite.spritecollide(self,enemy_group2,False)
        if hits5 or hits6:
            son_cri.play()
            self.Vy=0
            self.Nb_vie-=1
            if self.Nb_vie>=0:
                morte()
                self.pos=[self.X1, 0]
            if self.Nb_vie<0:
                gameover()
                return False

####MORT

        hits2 = pg.sprite.spritecollide(self, death, False)
        if hits2:
            son_cri.play()
            self.hit_rect.centerx = self.pos[0]
            collide(self,death, 'x')
            self.hit_rect.centery = self.pos[1]
            collide(self, death, 'y')
            self.Vy=0
            self.Nb_vie-=1
            if self.Nb_vie>=0:
                morte()
                self.pos=[self.X1, 0]
            if self.Nb_vie<0:
                gameover()
                return False
 
#####GAGNER           

        hits3 = pg.sprite.spritecollide(self,go,False)
        if hits3:
            son_gagne.play()
            self.hit_rect.centerx = self.pos[0]
            collide(self,go, 'x')
            self.hit_rect.centery = self.pos[1]
            collide(self, go, 'y')
            self.Vy=0
            gagner()
            return False
        return True

player=Player(100, 1700)





        
