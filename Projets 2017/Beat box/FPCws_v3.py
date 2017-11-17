import pygame
import time
import pyaudio
import wave
from pygame.locals import *

#	Classe Bouton que possede 10 propriete et 3 fonction. Il existe actuellement 3 types d espece de bouton. Volume, son et enregistrent 	#
class Bouton : 																			
    def __init__(self, son, couleur, appuyer, position, x, y, t, espece, name):
    	# Definition des proprietes de la classe bouton#
        self.name= name
        self.son = son                                                          
        self.channel = pygame.mixer.Channel(x)
        self.couleur = couleur                                                  
        self.appuyer = False                                                    
        self.position_carte = position                                          
        self.position_rel= [x,y]                                                
        self.thickness = t
        self.espece = espece
        self.rect = 0
                                          

    def appuyerB(self):     
    # Fonction que change l etat logic du bouton d etre appuyer#                                                           
        
        if self.appuyer == True :
            self.appuyer= False
        else:
            self.appuyer= True

    def dessinerB(self):
    # Fonction que dessine les bouton sur l ecran, dependant de l espece du bouton, des parametres diferrents seront initialiser#
        
        for i in range(4):
            if self.position_rel[0]== i and self.espece=="son":
                self.rect=pygame.draw.rect(screen, self.couleur, self.position_carte, self.thickness)
            elif self.position_rel[0]== i and self.espece=="volume":	# A chaque foi que l on dessine les bouton de volume, le volume proprement dit est actualiser
                pygame.draw.line(screen, [255,255,255], [1245,122.5+230*i], [1445,122.5+230*i], 2)
                self.rect=pygame.draw.rect(screen, self.couleur, self.position_carte, self.thickness)
                vol = (self.rect.x - 1245) / 200
                self.channel.set_volume(vol)
            elif self.espece=="enreg":
                self.rect=pygame.draw.rect(screen, self.couleur, self.position_carte, self.thickness)
   
                
                
        
    def Clinoter(self,screen):  
    # Fonction que donne un aspect estetique, lorsque l utilisateu attends le prochain son rentre au meme tempo# 
        
        if self.thickness==0: 		# Si la grosseur est 0 il la transforme em 5 et vice versa
            self.thickness = 5
        else:
            self.thickness = 0

def wait(start_time, tempo, B, screen, listeB):
# Fonction que fait l utilisateur attendre entre chaque tempo, de maniere a rentrer les son harmoniquement#

    time1 = start_time          #le temps ou l'on a commence a jouer le premier son.          
    padrao= B.thickness         #maintenir la grosseur appuyer
    while True:                 #On ne veut pas qu'il s'arrete
        time2 = time.time()     #le temps actuel
        if abs((time2 - time1)%tempo)  < 0.005: #calcule du reste de la division
            B.thickness= padrao #quand le son est lance, le bouton garde la thickness appuyer 
            break               #la condition (etre exactement au tempo) est ateinte donct on sort du while
        if abs((time2 - time1)%0.5)  < 0.001: #clignotement chaque 0.5s
            screen.blit(fond,(0,0)) #redessine tout pendant le clignotement 
            B.Clinoter(screen)
            for chaque_bouton in listeB : 
                chaque_bouton.dessinerB()
            pygame.display.flip()   #forcer le redessinement



def InitB(Couleurs):  
# Fonction d initialisation du programme, ele va creer tout les object que seront utiliser dans le programme#

    listeB = []                                                                 
    count = 1
    for i in range (4) :
        for j in range (4) :
            stringson= "son" + str(count) + ".wav"	# Le programme ne marche pas si les sont ne sont pas organizaer de la forma sonN.wav avec N variant de 1 a 16
            B= Bouton(pygame.mixer.Sound(stringson), Couleurs[j], False, [40+(i*290),30+(j*245), 250,185], j, i, 0, 'son', stringson)
            B.rect=pygame.draw.rect(screen, Couleurs[j], [40+(i*290),30+(j*245), 250,185], 0)
            listeB.append(B)                                                   
            count += 1
    for i in range(4):
        Volume = Bouton('', [100, 90, 145], False, [1345,112.5+(i*230), 20,20], i, 5, 0, 'volume', '')
        Volume.rect=pygame.draw.rect(screen, [100, 90, 145], [1345,112.5+(i*230), 20,20], 0)
        listeB.append(Volume)

    Enregistre=Bouton('', [40,40,40], False, [1310, 845, 82,90], 7, 7, 1, 'enreg', '')
    Enregistre.rect=pygame.draw.rect(screen, [40,40,40], [1310, 853, 82,90], 1)
    listeB.append(Enregistre)

    return listeB
 

def EpaisseurB(screen,listeB, x, y, rouge, vert, bleu, violet, start_time):     
# Fonction que travaille avec les collition du MOUSE de l utilisateur et les action du programme. C est l interactivite du programme#

    L_couleur = [rouge,vert,bleu,violet]
    if (L_couleur[0]==False and L_couleur[1]==False and L_couleur[2]==False and L_couleur[3]==False):   # Condition qui evite des wait non necessaire. Si tout les bouton sont d essapuyer, le programme pense qu'il est reinitialiser.
        start_time=0

    for B in listeB :     # Pour chaque element bouton de l'initialisation je verifier les possible collition du programme.          
        if B.rect.collidepoint((x,y)) and B.appuyer == True and B.espece == 'son' :
                                                                                
             for i in range (4):
                 if B.position_rel[0] == i and L_couleur[i] == True:
                     L_couleur[i] = False
                     B.thickness = 0
                     B.channel.stop()
                     B.appuyerB()
                     
        elif B.rect.collidepoint ((x,y)) and B.appuyer == False and B.espece == 'son'  :
             for i in range (4):
                 if B.position_rel[0] == i and L_couleur[i] == False and start_time==0:
                     L_couleur[i] = True
                     B.thickness = 5
                     B.channel.play(B.son, -1)
                     start_time=time.time()
                     B.appuyerB()

                 elif B.position_rel[0] == i and L_couleur[i] == False:
                     L_couleur[i] = True
                     B.thickness = 5
                     wait(start_time, 7.38, B, screen, listeB)
                     B.channel.play(B.son, -1)
                     B.appuyerB() 

                 elif B.position_rel[0] == i and L_couleur[i] == True:
                     for NB in listeB:
                         if NB.position_rel[0] == i and NB.appuyer == True and L_couleur[i] == True:
                            L_couleur[i] == False
                            NB.thickness = 0
                            wait(start_time, 7.38, B, screen, listeB)
                            NB.channel.stop()
                            NB.appuyerB()

                     L_couleur[i] == True
                     B.thickness = 5
                     B.channel.play(B.son, -1)
                     B.appuyerB()                                                  

        B.dessinerB()

    return L_couleur[0], L_couleur[1], L_couleur[2], L_couleur[3], start_time # Les variable couleur et temps sont important globalment, donc elles sont les input et sortie de la fonction epaisseur.


################################################################ Le programme Commence ###############################################################################      

fond_tut= pygame.image.load('fond_tutoriel.jpg')
pygame.init()  	# initialisation du programme

# Taille du programme
S = 1500                                                                        
V = 980                                                                         
size = 30  
screen = pygame.display.set_mode([S, V])

# Paramentres d enregistrement du programme
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 7.38
WAVE_OUTPUT_FILENAME = "output.wav"

# bloc de couleurs de chaque ligne:
Cgris=[100,100,100]
Cnoir=[0,0,0]
Crouge=[255,0,0]
Cvert=[0,255,0]
Cbleu=[0,0,255]
Crose=[255,0,100]
Couleurs= [Crouge, Cvert, Cbleu, Crose]

# initialisation des variable global necessaire pour le fonctionement du programme
rouge, vert, bleu, violet = False, False, False, False
Volume_draging = [False,False,False,False]
start_time = 0.0
pygame.mixer.init(frequency = 44100, size = -16, channels = 1, buffer = 2**12) 
running = True
tutoriel = True

#le bloc des figures a montrer
list_tutoriel=[]
list_tutoriel.append([pygame.Rect(100,100,200,200),False,pygame.Rect(600,100,600,200)])
list_tutoriel.append([pygame.Rect(100,400,200,200),False,pygame.Rect(600,400,600,200)])
list_tutoriel.append([pygame.Rect(100,700,200,200),False,pygame.Rect(600,700,600,200)])
sortie=pygame.Rect(1250,700,200,200)

# Premiere initilization du tutoriel, seulement 3 rectangle sont afficher, le reste doit etre noir.
screen.blit(fond_tut,(0,0)) 
for b_tutoriel in list_tutoriel:
	pygame.draw.rect(screen,Cnoir,b_tutoriel[2])

# Premier loop de tutoriel, qui explique le programme et parle des auteurs.
while tutoriel:

    for b_tutoriel in list_tutoriel:
        pygame.draw.rect(screen,Cgris,b_tutoriel[0],1)
    pygame.draw.rect(screen,Cgris,sortie,1)
    
    
    for e in pygame.event.get():
        if e.type == MOUSEBUTTONDOWN and e.button==1:
            x, y = e.pos
            if sortie.collidepoint((x,y)):
                tutoriel = False
            for b_tutoriel in list_tutoriel:
                if b_tutoriel[0].collidepoint((x,y)) and b_tutoriel[1]==False:	    # Si le bouton est appuyer du tutoriel, le texte correspondant est afficher
                    pygame.draw.rect(screen,Cgris,b_tutoriel[2],1)
                    b_tutoriel[1]=True
                    screen.blit(fond_tut,(0,0))
                    for b_tutoriel in list_tutoriel:
                    	if b_tutoriel[1]==False:		    # Si le bouton est dessapuyer on efface le texte correpondant.
                    		pygame.draw.rect(screen,Cnoir,b_tutoriel[2])
                elif b_tutoriel[0].collidepoint((x,y)) and b_tutoriel[1]==True:
                    pygame.draw.rect(screen,Cnoir,b_tutoriel[2])
                    b_tutoriel[1]=False

        if e.type == QUIT:				# si on apuyyer exit meme au tutoriel, le programme est fini
            running = False
            tutoriel = False
            pygame.quit()
                
                
                

      
    pygame.display.flip()


# Initilization du programme, apres le tutoriel, les liste sont initialiser et les image de l ecran changer.
fond = pygame.image.load('FOND1.jpg')
listeB = InitB(Couleurs)
Volumes=listeB[16:20]
Enregistre=listeB[-1]
while running:
    
    screen.blit(fond,(0,0))                                                     
    for e in pygame.event.get():

        if e.type == QUIT:
            running = False
            pygame.quit()
            
        if e.type == MOUSEBUTTONDOWN and e.button==1:
            x, y = e.pos
            if Enregistre.rect.collidepoint(e.pos):		# Partie de l enregistrement. l enregistrement est fait avec la biblioteque pyaudio. Le son est enregistrer par um microfone
                p = pyaudio.PyAudio()
                frames=[]
                stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
                print("* recording")
                for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                    data = stream.read(CHUNK)
                    frames.append(data)
                print("* done recording")
                stream.stop_stream()
                stream.close()
                p.terminate()

                wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(p.get_sample_size(FORMAT))
                wf.setframerate(RATE)
                wf.writeframes(b''.join(frames))
                wf.close()
                
            for Volume in Volumes:					# mouvement du bouton de volume, actualization de sa position.
                if Volume.rect.collidepoint(e.pos):
                        Volume_draging[Volumes.index(Volume)] = True
                        mouse_x, mouse_y = e.pos
                        offset_x = Volume.rect.x - mouse_x
                        offset_y = Volume.rect.y - mouse_y

        elif e.type == MOUSEBUTTONUP:
            if e.button == 1:            
                for i in range(4):
                    Volume_draging[i]=False
                    

        elif e.type == MOUSEMOTION:				# Limitation des coordonnees des bouton de volumes.
            for Volume in Volumes:
                if Volume_draging[Volumes.index(Volume)]:
                    mouse_x, mouse_y = e.pos
                    Volume.rect.x = mouse_x + offset_x
                    if Volume.rect.x > 1445:
                        Volume.rect.x = 1445
                    if Volume.rect.x < 1245:
                        Volume.rect.x = 1245
                
   
    for Volume in Volumes:
        Volume.position_carte=[Volume.rect.x,Volume.rect.y, 20,20]   
    rouge, vert, bleu, violet, start_time = EpaisseurB(screen,listeB, x, y, rouge, vert, bleu, violet, start_time)
    pygame.display.flip()
    x, y = 0, 0  
