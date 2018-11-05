import pygame
import time
import math
import random


pygame.init()

pygame.mixer.init()

longueur = 1050
largeur = 750

epaisseurLigne = 7

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

vitesseBalle = 0

ecran = pygame.display.set_mode((0,0))
pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')
clock = pygame.time.Clock()

fond = pygame.image.load('fond etoile.jpg')

class balle(pygame.sprite.Sprite):
        def __init__(self,x,y,vx,vy):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('boule2.jpg')
            self.x = x
            self.y = y
            self.rect = pygame.Rect(x,y,27,27)
            self.vx = vx
            self.vy = vy

        def afficher(self):
            ecran.blit(self.image,(self.x,self.y))

        def mouvement(self):
                   self.x += self.vx
                   self.y += self.vy


class mur(pygame.sprite.Sprite):
        def __init__(self,a,b,c,d):
            pygame.sprite.Sprite.__init__(self)
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.rect = pygame.Rect(a,b,c,d)

        def afficher(self):
            pygame.draw.rect(ecran,white,self.rect)


def checkCollision(sprite1, sprite2):
        if pygame.sprite.collide_rect(sprite1, sprite2):
                return True
        else:
                return False


class raquette(pygame.sprite.Sprite):
        def __init__(self,x,y):
             pygame.sprite.Sprite.__init__(self)
             self.image = pygame.image.load('raquette2.jpg')
             self.image2 = pygame.image.load('raquette3.jpg')
             self.x = x
             self.y = y
             self.vitesse = 0
             self.rect = pygame.Rect(x,y,15,150)

        def afficher(self):
             ecran.blit(self.image,(self.x,self.y))

        def afficher2(self):
             ecran.blit(self.image2,(self.x,self.y))


class raquetteExtreme(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.vitesse = 0
            self.rect = pygame.Rect(x,y,15,30)


def Son(x):
        son = pygame.mixer.Sound(x)
        son.set_volume(0.1)
        #print (son.get_volume())
        pygame.mixer.Sound.play(son)

def EcranNoirTexte(texte,x,y,temps):
        ecran.fill(black)
        messageDisparition(texte,x,y,temps)


def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def messageDisparition(text,x,y,temps):
    font = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = ((x),(y))
    ecran.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(temps)

def AffichageTexte(text,x,y,taille):
    font = pygame.font.Font('FORTE.ttf',taille)
    TextSurf, TextRect = text_objects(text, font)
    TextRect.center = (x,y)
    ecran.blit(TextSurf, TextRect)


def ligne():
        pygame.draw.line(ecran,white,(longueur/2,70),(longueur/2, largeur),epaisseurLigne)


def anglerandom():
        angle1 = random.randint(-30,30)
        angle2 = random.randint(150,210)

        angles = [angle1,angle2]
        angle = random.choice(angles)
        print(angle)
        angle = math.radians(angle)
        return angle

def prenom(x):
        screen = pygame.display.set_mode((480, 360))
        prenom = ""
        font = pygame.font.Font(None, 50)
        sortir = False
        while sortir == False:
                for evt in pygame.event.get():
                    if evt.type == pygame.KEYDOWN:
                        if evt.unicode.isalpha():
                                prenom += evt.unicode
                        elif evt.key == pygame.K_BACKSPACE:
                                prenom = prenom[:-1]
                        elif evt.key == pygame.K_RETURN:
                                return prenom
                                sortir = True
                    elif evt.type == pygame.QUIT:
                        return prenom
                        sortir = True

                screen.fill(black)
                AffichageTexte(x,150,40,50)
                AffichageTexte(prenom,240,180,50)
                pygame.display.flip()

def verification():
    ecran = pygame.display.set_mode((longueur,largeur))
    pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')
    clock = pygame.time.Clock()
    bouton=pygame.draw.rect(ecran,green,(145,315,235,120))
    bouton1=pygame.draw.rect(ecran,red,(670,315,235,120))
    finir = False

    while finir == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN :
              if event.button == 1 :
                  if bouton.collidepoint(event.pos):
                      return True
                      finir = True
                  if bouton1.collidepoint(event.pos):
                      finir = True
        ecran.fill(black)
        pygame.draw.rect(ecran,red,(145,335,235,120))
        pygame.draw.rect(ecran,green,(670,335,235,120))
        AffichageTexte('Oui',255,395,50)
        AffichageTexte('Non',790,395,50)
        AffichageTexte('Êtes-vous sûr de vouloir quitter ?',525,130,70)
        pygame.display.update()
        clock.tick(60)


def pageTouches():

    ecran = pygame.display.set_mode((600,400))

    ecran.fill(black)

    pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')

    clock = pygame.time.Clock()



    sortir = False

    while sortir ==False:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                ecran = pygame.display.set_mode((740,740))

                sortir = True

            if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:

                        ecran = pygame.display.set_mode((740,740))

                        sortir = True



        AffichageTexte(('J 1:'+'    '+'Monter:   W'+'   '+'Descendre:   S'),300,200,30)

        AffichageTexte('J 2:'+'    '+'Monter: Fleche haut'+'   '+'Descendre: Fleche bas',300,250,26)

        pygame.display.update()

        clock.tick(60)




def menuNiveaux():
    ecran = pygame.display.set_mode((740,740))
    pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')
    clock = pygame.time.Clock()
    button=pygame.draw.rect(ecran,blue,(250,200,235,120))
    button2=pygame.draw.rect(ecran,blue,(250,410,235,120))
    button3=pygame.draw.rect(ecran,blue,(250,600,235,120))
    jouer1 = jeu(8,7,0)
    jouer2 = jeu(10,7,0)
    jouer3 = jeu(20,15,0)

    sortir = False
    while sortir == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sortir=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sortir = True
            if event.type == pygame.MOUSEBUTTONDOWN :
              if event.button == 1 :
                  if button.collidepoint(event.pos):
                      jouer1.run()
                      sortir = True
                  if button2.collidepoint(event.pos):
                      jouer2.run()
                      sortir = True
                  if button3.collidepoint(event.pos):
                      jouer3.run()
                      sortir = True
        ecran.blit(fond,(0,0))
        pygame.draw.rect(ecran,blue,(250,200,235,120))
        pygame.draw.rect(ecran,blue,(250,410,235,120))
        pygame.draw.rect(ecran,blue,(250,600,235,120))
        AffichageTexte('Niveau 1',370,250,50)
        AffichageTexte('Niveau 2',370,460,50)
        AffichageTexte('Niveau 3',370,650,50)
        AffichageTexte('Niveaux :',370,100,70)
        pygame.display.update()
        clock.tick(15)



def menu():
    ecran = pygame.display.set_mode((740,740))
    pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')
    clock = pygame.time.Clock()
    button=pygame.draw.rect(ecran,green,(270,200,200,120))
    button2=pygame.draw.rect(ecran,red,(270,520,200,120))
    button3=pygame.draw.rect(ecran,blue,(270,360,200,120))
    button4=pygame.draw.rect(ecran,red,(600,20,100,50))

    EcranNoirTexte('Teo,Eliott et Mathias',370,370,1)
    jouerAI = jeu(10,7,7)

    sortir = False
    while sortir ==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sortir=True
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_RETURN:
                    #jeu()
            if event.type == pygame.MOUSEBUTTONDOWN :
              if event.button == 1 :
                  if button.collidepoint(event.pos):
                      menuNiveaux()
                  if button2.collidepoint(event.pos):
                      sortir=True
                  if button3.collidepoint(event.pos):
                      jouerAI.runAI()
                  if button4.collidepoint(event.pos):
                      pageTouches()

        ecran.blit(fond,(0,0))
        pygame.draw.rect(ecran,green,(270,200,200,120))
        pygame.draw.rect(ecran,red,(270,520,200,120))
        pygame.draw.rect(ecran,blue,(270,360,200,120))
        pygame.draw.rect(ecran,red,(600,20,100,50))

        AffichageTexte('1 VS 1',370,260,50)
        AffichageTexte('Quitter',370,580,50)
        AffichageTexte('1 V Ai',370,420,50)
        AffichageTexte("Aide?",650,44,30)

        AffichageTexte('Pong v2',370,100,70)
        AffichageTexte('Teo, Eliott et Mathias',610,700,20)
        pygame.display.update()
        clock.tick(15)


class jeu():
    def __init__(self,vitesseBalle,vitesseRaquette,vitesseAI):
        self.vitesseBalle = vitesseBalle
        self.vitesseRaquette = vitesseRaquette
        self.vitesseDepart =  self.vitesseBalle
        self.vitesseDepartRaquette = self.vitesseRaquette
        self.vitesseAI = vitesseAI
        pygame.display.set_caption('Pong v2 (Teo, Eliott et Mathias)')

        self.clock = pygame.time.Clock()
        self.temps = 0
        self.seconde = 0
        self.minute = 0

        self.raquettegaucheX= 48
        self.raquettegaucheY= 300
        self.raquettedroiteX = 976
        self.raquettedroiteY = 300
        self.balleX= 525
        self.balleY= 375

        self.Score1 = 0
        self.Score2 = 0


        self.angle = anglerandom()
        self.vx = self.vitesseBalle * (math.cos(self.angle))
        self.vy = self.vitesseBalle * (math.sin(self.angle))


        self.ballepong = balle(self.balleX,self.balleY,self.vx,self.vy)
        self.raquettegauche =raquette(self.raquettegaucheX,self.raquettegaucheY)
        self.raquettegaucheExtremeHaut = raquetteExtreme(self.raquettegaucheX,self.raquettegaucheY)
        self.raquettegaucheExtremeBas = raquetteExtreme(self.raquettegaucheX,self.raquettegaucheY+120)


        #print(id(r))
        self.raquettedroite =raquette(self.raquettedroiteX,self.raquettedroiteY)
        self.raquettedroiteExtremeHaut =raquetteExtreme(self.raquettedroiteX,self.raquettedroiteY)
        self.raquettedroiteExtremeBas =raquetteExtreme(self.raquettedroiteX,self.raquettedroiteY+120)

        #raquettegauche.afficher()
        self.raquettegauche.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY,15,150)

        self.raquettegaucheExtremeHaut.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY,15,30)
        self.raquettegaucheExtremeBas.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY+120,15,30)

        #raquettedroite.afficher()
        self.raquettedroite.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY,15,150)

        self.raquettedroiteExtremeHaut.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY,15,30)
        self.raquettedroiteExtremeBas.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY+120,15,30)

        self.murhaut = mur(0,70,1050,7)
        self.murbas = mur(0,745,1050,7)


    def run(self):
            prenom1 = prenom("Joueur 1 : ")
            prenom2 = prenom("Joueur 2 : ")
            ecran = pygame.display.set_mode((longueur,largeur))
            sortir = False

            while not sortir:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            if verification() == True:
                                        ecran = pygame.display.set_mode((740,740))
                                        sortir = True

                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                if verification() == True:
                                        ecran = pygame.display.set_mode((740,740))
                                        sortir = True



                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            self.raquettegauche.vitesse = -self.vitesseRaquette

                        if event.key == pygame.K_s:
                            self.raquettegauche.vitesse = self.vitesseRaquette


                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            self.raquettegauche.vitesse = 0

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                           self.raquettedroite.vitesse = -self.vitesseRaquette
                        if event.key == pygame.K_DOWN:
                           self.raquettedroite.vitesse = self.vitesseRaquette

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            self.raquettedroite.vitesse = 0

                if((self.raquettegauche.y+self.raquettegauche.vitesse)> 77 and (self.raquettegauche.y+self.raquettegauche.vitesse)<(580)):
                    self.raquettegauche.y += self.raquettegauche.vitesse
                    self.raquettegaucheExtremeHaut.y += self.raquettegauche.vitesse
                    self.raquettegaucheExtremeBas.y += self.raquettegauche.vitesse+120
                if((self.raquettedroite.y+self.raquettedroite.vitesse)> 77 and (self.raquettedroite.y+self.raquettedroite.vitesse)<(580)):
                    self.raquettedroite.y += self.raquettedroite.vitesse
                    self.raquettedroiteExtremeHaut.y += self.raquettedroite.vitesse
                    self.raquettedroiteExtremeBas.y += self.raquettedroite.vitesse+120


                ecran.fill(black)
                ligne()

                score1 = str(self.Score1)
                AffichageTexte(score1,250,40,50)

                score2 = str(self.Score2)
                AffichageTexte(score2,790,40,50)



                self.raquettegauche.afficher()
                self.raquettegauche.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y,15,150)
                self.raquettegaucheExtremeHaut.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y,15,30)
                self.raquettegaucheExtremeBas.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y+120,15,30)
                self.raquettedroite.afficher2()
                self.raquettedroite.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y,15,150)
                self.raquettedroiteExtremeHaut.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y,15,30)
                self.raquettedroiteExtremeBas.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y+120,15,30)

                #pygame.draw.rect(ecran,green,self.raquettegauche.rect)
                #pygame.draw.rect(ecran,green,raquettedroiteExtremeHaut.rect)
                #pygame.draw.rect(ecran,red,raquettedroiteExtremeBas.rect)
                #pygame.draw.rect(ecran,green,raquettegaucheExtremeHaut.rect)
                #pygame.draw.rect(ecran,red,raquettegaucheExtremeBas.rect)
                #pygame.draw.rect(ecran,red,self.ballepong.rect)

                self.murhaut.afficher()
                self.murbas.afficher()


                self.ballepong.afficher()
                self.ballepong.mouvement()

                self.ballepong.rect = pygame.Rect(self.ballepong.x,self.ballepong.y,30,30)

                if checkCollision(self.ballepong,self.raquettegauche) == True and checkCollision(self.ballepong,self.raquettegaucheExtremeHaut) == False and checkCollision(self.ballepong,self.raquettegaucheExtremeBas) == False:
                        Son("pong.wav")
                        self.ballepong.vx = -self.ballepong.vx

                if checkCollision(self.ballepong,self.raquettegaucheExtremeHaut) == True:
                        Son("pong.wav")
                        self.vitesseRaquette += 1
                        self.vitesseBalle += 1
                        self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(-50)))
                        self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(-50)))

                if checkCollision(self.ballepong,self.raquettegaucheExtremeBas) == True:
                        Son("pong.wav")
                        self.vitesseRaquette += 1
                        self.vitesseBalle += 1
                        self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(50)))
                        self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(50)))

                if checkCollision(self.ballepong,self.raquettedroite) == True and checkCollision(self.ballepong,self.raquettedroiteExtremeHaut) == False and checkCollision(self.ballepong,self.raquettedroiteExtremeBas) == False:
                        Son("pong.wav")
                        self.ballepong.vx = -self.ballepong.vx

                if checkCollision(self.ballepong,self.raquettedroiteExtremeHaut) == True:
                        Son("pong.wav")
                        self.vitesseRaquette += 1
                        self.vitesseBalle += 1
                        self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(230)))
                        self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(230)))

                if checkCollision(self.ballepong,self.raquettedroiteExtremeBas) == True:
                        Son("pong.wav")
                        self.vitesseRaquette += 1
                        self.vitesseBalle += 1
                        self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(130)))
                        self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(130)))


                if checkCollision(self.ballepong,self.murhaut) == True:
                        self.ballepong.vy = -self.ballepong.vy

                if checkCollision(self.ballepong,self.murbas) == True:
                        self.ballepong.vy = -self.ballepong.vy



                if self.ballepong.x < 15:
                        time.sleep(0.25)
                        self.vitesseRaquette = self.vitesseDepartRaquette
                        self.vitesseBalle = self.vitesseDepart
                        if self.Score2 + 1 == 5:
                                Son("applaudissement.wav")
                                EcranNoirTexte("Vainqueur : " + prenom2,525,375,1.3)
                                ecran = pygame.display.set_mode((740,740))
                                sortir = True
                        else:
                                Son("but.wav")
                                EcranNoirTexte("BUT !!!  " + prenom2,525,375,1.3)
                                self.Score2 += 1
                        jeu.reset(self)

                elif self.ballepong.x >1010:
                        time.sleep(0.25)
                        self.vitesseRaquette = self.vitesseDepartRaquette
                        self.vitesseBalle = self.vitesseDepart
                        if self.Score1 + 1 == 5:
                                Son("applaudissement.wav")
                                EcranNoirTexte("Vainqueur : " + prenom1,525,375,1.3)
                                ecran = pygame.display.set_mode((740,740))
                                sortir = True
                        else:
                                Son("but.wav")
                                EcranNoirTexte("BUT !!!  " + prenom1,525,375,1.3)
                                self.Score1 += 1
                        jeu.reset(self)

                self.temps +=1
                if self.temps % 60 == 0:
                         self.seconde +=1
                if self.seconde > 0:
                         if self.seconde % 60 == 0:
                                 self.minute += 1
                                 self.seconde = 0
                minuteAffichage = str(self.minute)
                secondeAffichage = str(self.seconde)
                if self.seconde < 10:
                         AffichageTexte("0"+secondeAffichage,560,40,50)
                if self.seconde >= 10:
                         AffichageTexte(secondeAffichage,560,40,50)
                if self.minute < 10:
                         AffichageTexte("0"+minuteAffichage,490,40,50)
                if self.minute >= 10:
                         AffichageTexte(minuteAffichage,490,40,50)
                AffichageTexte(":",525,40,50)
                pygame.display.update()
                self.clock.tick(60)


    def runAI(self):
        prenom1 = prenom("Joueur 1 : ")
        ecran = pygame.display.set_mode((longueur,largeur))
        sortir = False

        while not sortir:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        if verification() == True:
                                    ecran = pygame.display.set_mode((740,740))
                                    sortir = True

                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if verification() == True:
                                    ecran = pygame.display.set_mode((740,740))
                                    sortir = True


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.raquettegauche.vitesse = -self.vitesseRaquette

                    if event.key == pygame.K_s:
                        self.raquettegauche.vitesse = self.vitesseRaquette


                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        self.raquettegauche.vitesse = 0


            if((self.raquettegauche.y+self.raquettegauche.vitesse)> 77 and (self.raquettegauche.y+self.raquettegauche.vitesse)<(580)):
                self.raquettegauche.y += self.raquettegauche.vitesse
                self.raquettegaucheExtremeHaut.y += self.raquettegauche.vitesse
                self.raquettegaucheExtremeBas.y += self.raquettegauche.vitesse+120



            distance = (self.raquettedroite.y+75)-self.ballepong.y
            #print(distance)
            if distance > 1:
                    if self.raquettedroite.y-self.vitesseAI > 77 and self.raquettedroite.y-self.vitesseAI < 580:   #Centre de l'image (+75)
                                self.raquettedroite.y -= self.vitesseAI
            if distance < -1:
                    if self.raquettedroite.y+self.vitesseAI > 77 and self.raquettedroite.y+self.vitesseAI < 580:
                                self.raquettedroite.y += self.vitesseAI


            ecran.fill(black)
            ligne()

            score1 = str(self.Score1)
            AffichageTexte(score1,250,40,50)

            score2 = str(self.Score2)
            AffichageTexte(score2,790,40,50)



            self.raquettegauche.afficher()
            self.raquettegauche.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y,15,150)
            self.raquettegaucheExtremeHaut.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y,15,30)
            self.raquettegaucheExtremeBas.rect = pygame.Rect(self.raquettegauche.x,self.raquettegauche.y+120,15,30)
            self.raquettedroite.afficher2()
            self.raquettedroite.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y,15,150)
            self.raquettedroiteExtremeHaut.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y,15,30)
            self.raquettedroiteExtremeBas.rect = pygame.Rect(self.raquettedroite.x,self.raquettedroite.y+120,15,30)

            #pygame.draw.rect(ecran,green,raquettegauche.rect)
            #pygame.draw.rect(ecran,green,raquettedroiteExtremeHaut.rect)
            #pygame.draw.rect(ecran,red,raquettedroiteExtremeBas.rect)
            #pygame.draw.rect(ecran,green,raquettegaucheExtremeHaut.rect)
            #pygame.draw.rect(ecran,red,raquettegaucheExtremeBas.rect)
            #pygame.draw.rect(ecran,red,ballepong.rect)


            self.murhaut.afficher()
            self.murbas.afficher()


            self.ballepong.afficher()
            self.ballepong.mouvement()

            self.ballepong.rect = pygame.Rect(self.ballepong.x,self.ballepong.y,30,30)




            if checkCollision(self.ballepong,self.raquettegauche) == True and checkCollision(self.ballepong,self.raquettegaucheExtremeHaut) == False and checkCollision(self.ballepong,self.raquettegaucheExtremeBas) == False:
                    Son("pong.wav")
                    self.ballepong.vx = -self.ballepong.vx

            if checkCollision(self.ballepong,self.raquettegaucheExtremeHaut) == True:
                    Son("pong.wav")
                    self.vitesseRaquette += 1
                    self.vitesseBalle += 1
                    self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(-50)))
                    self.ballepong.vy =  self.vitesseBalle * (math.sin(math.radians(-50)))

            if checkCollision(self.ballepong,self.raquettegaucheExtremeBas) == True:
                    Son("pong.wav")
                    self.vitesseRaquette += 1
                    self.vitesseBalle += 1
                    self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(50)))
                    self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(50)))

            if checkCollision(self.ballepong,self.raquettedroite) == True and checkCollision(self.ballepong,self.raquettedroiteExtremeHaut) == False and checkCollision(self.ballepong,self.raquettedroiteExtremeBas) == False:
                    Son("pong.wav")
                    self.ballepong.vx = -self.ballepong.vx

            if checkCollision(self.ballepong,self.raquettedroiteExtremeHaut) == True:
                    Son("pong.wav")
                    self.vitesseRaquette += 1
                    self.vitesseBalle += 1
                    self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(230)))
                    self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(230)))

            if checkCollision(self.ballepong,self.raquettedroiteExtremeBas) == True:
                    Son("pong.wav")
                    self.vitesseRaquette += 1
                    self.vitesseBalle += 1
                    self.ballepong.vx = self.vitesseBalle * (math.cos(math.radians(130)))
                    self.ballepong.vy = self.vitesseBalle * (math.sin(math.radians(130)))


            if checkCollision(self.ballepong,self.murhaut) == True:
                    self.ballepong.vy = -self.ballepong.vy

            if checkCollision(self.ballepong,self.murbas) == True:
                    self.ballepong.vy = -self.ballepong.vy


            if self.ballepong.x < 15:
                    time.sleep(0.25)
                    self.vitesseRaquette = self.vitesseDepartRaquette
                    self.vitesseBalle = self.vitesseDepart
                    if self.Score2 + 1 == 5:
                            Son("applaudissement.wav")
                            EcranNoirTexte("Vainqueur : " + "ORDI",525,375,1.3)
                            ecran = pygame.display.set_mode((740,740))
                            sortir = True
                    else:
                            Son("but.wav")
                            EcranNoirTexte("BUT !!! " + "ORDI",525,375,1.3)
                            self.Score2 += 1
                    jeu.reset(self)

            elif self.ballepong.x >1010:
                    time.sleep(0.25)
                    self.vitesseRaquette = self.vitesseDepartRaquette
                    self.vitesseBalle = self.vitesseDepart
                    if self.Score1 + 1 == 5:
                            Son("applaudissement.wav")
                            EcranNoirTexte("Vainqueur : " + prenom1,525,375,1.3)
                            ecran = pygame.display.set_mode((740,740))
                            sortir = True
                    else:
                            Son("but.wav")
                            EcranNoirTexte("BUT !!!  " + prenom1,525,375,1.3)
                            self.Score1 += 1
                    jeu.reset(self)



            self.temps +=1
            if self.temps % 60 == 0:
                     self.seconde +=1
            if self.seconde > 0:
                     if self.seconde % 60 == 0:
                             self.minute += 1
                             self.seconde = 0
            minuteAffichage = str(self.minute)
            secondeAffichage = str(self.seconde)
            if self.seconde < 10:
                     AffichageTexte("0"+secondeAffichage,560,40,50)
            if self.seconde >= 10:
                     AffichageTexte(secondeAffichage,560,40,50)
            if self.minute < 10:
                     AffichageTexte("0"+minuteAffichage,490,40,50)
            if self.minute >= 10:
                     AffichageTexte(minuteAffichage,490,40,50)
            AffichageTexte(":",525,40,50)
            pygame.display.update()
            self.clock.tick(60)

    def reset(self):
                        self.angle = anglerandom()
                        self.ballepong.vx = self.vitesseBalle * (math.cos(self.angle))
                        self.ballepong.vy = self.vitesseBalle * (math.sin(self.angle))

                        self.ballepong.x = 525
                        self.ballepong.y = 375
                        self.ballepong.rect = pygame.Rect(self.balleX,self.balleY,30,30)
                        self.raquettegauche.x = 48
                        self.raquettegauche.y = 300
                        self.raquettegauche.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY,15,150)
                        self.raquettegaucheExtremeHaut.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY,15,30)
                        self.raquettegaucheExtremeBas.rect = pygame.Rect(self.raquettegaucheX,self.raquettegaucheY+120,15,30)
                        self.raquettedroite.x = 976
                        self.raquettedroite.y = 300
                        self.raquettedroite.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY,15,150)
                        self.raquettedroiteExtremeHaut.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY,15,30)
                        self.raquettedroiteExtremeBas.rect = pygame.Rect(self.raquettedroiteX,self.raquettedroiteY+120,15,30)


menu()
pygame.mixer.quit()
pygame.quit()
quit()
