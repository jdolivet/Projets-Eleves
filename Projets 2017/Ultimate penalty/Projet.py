import pygame
import os
import random

from Objets import *

# paramètres qui ne changent pas lors de retirer
score = 0
gardien_pris = 0
isolé = 0
tentatives = 0
fps = 25
Tutorial = True
reiniciar = True
Introduction = True # Pour faire l'intro
InterfaceTutoriel = 0
running = True
son = False
infini = False

# Initialiser pygame et créer une écran
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tirs de Pénalty")
clock = pygame.time.Clock()
icn = pygame.image.load(os.path.join(img_folder, "icon.jpg"))
pygame.display.set_icon(icn)
keystate = pygame.key.get_pressed()


from Fonctions import *

# Boucle de l'intérface tutoriel
while Introduction:
    if InterfaceTutoriel == 0:
        intro = Intro()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.wait(2000)
        all_sprites.remove(intro)
        Intro.kill(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        InterfaceTutoriel = 1

    if 3 > InterfaceTutoriel > 1: # Pour retourner une page
        screen.blit(flèchegauche, (15, 600))

    if InterfaceTutoriel < 2:  # pour avancer une page
        screen.blit(flèchedroite, (935, 600))

    if InterfaceTutoriel >= 1:
        Intro.kill(intro)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(bg, (0, 0))
        if InterfaceTutoriel == 1:
            screen.blit(jouer, (392.5, 364))
            if infini:
                screen.blit(image_infinie, (50, 40))
            if not infini:
                screen.blit(image_pasinfinie, (50, 40))
            if son :
                screen.blit(image_son, (850,40))
            if not son:
                screen.blit(image_pas_son, (850, 40))

        if InterfaceTutoriel == 2:
            draw_text(screen, "Tutoriel", 35, 500, 50, green)
            draw_text(screen, "Pour jouer à ce jeux, vous devez cliquer que deux fois sur le clavier:", 25, 500, 100, black)
            draw_text(screen, "Une première fois sur l'espace pour déterminer la précision de votre tir", 25, 500, 150, black)
            draw_text(screen, "évidemment que c'est sur le vert que vous voulez appuyer pour la meilleur précision", 25, 500, 200, black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            Introduction = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                Introduction = False
            if event.key == pygame.K_RIGHT:
                InterfaceTutoriel += 1
            if event.key == pygame.K_LEFT:
                if InterfaceTutoriel > 1:
                    InterfaceTutoriel -= 1

        if event.type == pygame.MOUSEBUTTONDOWN: # event.pos[o] = x et event.pos[1] = y
            if event.pos[0] >= 935 and event.pos[0] <= 985 and event.pos[1] >= 600 and event.pos[1] <= 640 and InterfaceTutoriel < 2:
                InterfaceTutoriel += 1
            if event.pos[0] >= 15 and event.pos[0] <= 65 and event.pos[1] >= 600 and event.pos[1] <= 640 and InterfaceTutoriel > 1:
                InterfaceTutoriel -= 1
            if event.pos[0] >= 393.5 and event.pos[0] <= 606.5 and event.pos[1] >= 364 and event.pos[1] <= 436 and InterfaceTutoriel == 1:
                Introduction = False
            if event.pos[0] >= 850 and event.pos[0] <= 947 and event.pos[1] >= 40 and event.pos[1] <= 116 and InterfaceTutoriel == 1:
                son = not son
            if event.pos[0] >= 50 and event.pos[0] <= 153 and event.pos[1] >= 40 and event.pos[1] <= 88 and InterfaceTutoriel == 1:
                infini = not infini

# Boucle du jeu
while running:

    clock.tick(fps)

    # pour retirer
    if reiniciar:
        reiniciar = False # pour retourner cette boucle ert rejouer le jeu
        direction = False # le joueur a donné la direction
        Tir_précision = False
        flèches_sur_lécran = True  # Les flèches sont ou pas sur l'écran
        direction_détérminée = False  # La direction est déterminée ou pas
        saut_déterminé = False
        paramètres_appliqués = False
        t6 = True
        sy = 0
        sx = 0
        st = 0
        saut = 0
        all_sprites = pygame.sprite.Group()
        player = Player()
        terrain = Terrain()
        ballon = Ballon()
        gardien = Gardien()
        barredeforce = BarredeForce()
        flechedeforce = FlèchedeForce()
        barredeprécision = BarredePrécision()
        flechedeprécision = FlèchedePrécision()
        all_sprites.add(terrain, gardien, ballon, player, barredeforce, flechedeforce, barredeprécision,
                        flechedeprécision)
        sound = True

    # pour montrer l'image de sortie
    def gExit():   # Teve de definit aqui para ser depois da definiçao de all_sprites
        all_sprites.remove(all_sprites)
        exit = ExitImage()
        all_sprites.update()
        all_sprites.add(exit)
        all_sprites.update()
        team = pygame.image.load(os.path.join(img_folder, "Team1.jpg"))
        pygame.display.set_mode((width, height)).blit(team, (0, 0))
        pygame.display.update()

    '''Si l'on veut limiter le nombre de chances'''
    if tentatives == 5 and not infini:
        reiniciar = False
        all_sprites.remove(all_sprites)
        all_sprites.update(all_sprites)
        all_sprites.draw(screen)
        screen.blit(bg, (0, 0))
        screen.blit(rejouer, (360.5, 355))
        draw_text(screen, "Vous avez marqué " + str(score) + " buts", 30, 500, 30)
        draw_text(screen, "Le gardien a encaissé " + str(gardien_pris) + " tirs", 30, 500, 60)
        draw_text(screen, "Vous avez mal cadré " + str(isolé) + " tirs", 30, 500, 90)
        pygame.display.flip()

        # pouvoir cliquer sur le bouton de rejouer
        if event.type == pygame.MOUSEBUTTONDOWN: # event.pos[o] = x et event.pos[1] = y
            if event.pos[0] >= 360.5 and event.pos[0] <= 639.5 and event.pos[1] >= 355 and event.pos[1] <= 445:
                tentatives = 0
                score = 0
                gardien_pris = 0
                isolé = 0
                reiniciar = True

    if flechedeforce.force_déterminée and flèches_sur_lécran: # Faire les flèches disparaître une fois les paramètres déterminés, en incluant la direction
        pygame.time.wait(2000)
        BarredePrécision.kill(barredeprécision)
        BarredeForce.kill(barredeforce)
        FlèchedeForce.kill(flechedeforce)
        FlèchedePrécision.kill(flechedeprécision)
        flèches_sur_lécran = False

    for event in pygame.event.get():

        # pouvoir quitter le jeu quand on appuye sur le x
        if event.type == pygame.QUIT: #Pour pouvoir sortir du jeu, et montrer l'image de sortie
            gExit()
            pygame.time.wait(2000)
            running = False

        # pour sortir du jeu si on appuye esc
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gExit()
                pygame.time.wait(2000)
                running = False
            if event.key == pygame.K_r:
                reiniciar = True

        #determiner la direction du tir en appuyant sur le clavier
        if event.type == pygame.KEYDOWN and flechedeforce.force_déterminée and not direction_détérminée:

            if event.key == pygame.K_q:
                direction = 1
                direction_détérminée = True

            elif event.key == pygame.K_w:
                direction = 2
                direction_détérminée = True

            elif event.key == pygame.K_e:
                direction = 3
                direction_détérminée = True

            elif event.key == pygame.K_a:
                direction = 4
                direction_détérminée = True

            elif event.key == pygame.K_s:
                direction = 5
                direction_détérminée = True

            elif event.key == pygame.K_d:
                direction = 6
                direction_détérminée = True

        # déterminer la direction du tir en cliquant sur l'écran
        if event.type == pygame.MOUSEBUTTONDOWN and flechedeforce.force_déterminée and not direction_détérminée:# event.pos[o] = x et event.pos[1] = y
            if event.pos[0] >= 250 and event.pos[0] <= 428 and event.pos[1] >= 99 and event.pos[1] <= 160:
                direction = 1
                direction_détérminée = True

            elif event.pos[0] >= 429 and event.pos[0] <= 599 and event.pos[1] >= 99 and event.pos[1] <= 160:
                direction = 2
                direction_détérminée = True

            elif event.pos[0] >= 600 and event.pos[0] <= 750 and event.pos[1] >= 99 and event.pos[1] <= 160:
                direction = 3
                direction_détérminée = True

            elif event.pos[0] >= 250 and event.pos[0] <= 428 and event.pos[1] >= 161 and event.pos[1] <= 322:
                direction = 4
                direction_détérminée = True

            elif event.pos[0] >= 429 and event.pos[0] <= 599 and event.pos[1] >= 161 and event.pos[1] <= 322:
                direction = 5
                direction_détérminée = True

            elif event.pos[0] >= 600 and event.pos[0] <= 750 and event.pos[1] >= 161 and event.pos[1] <= 322:
                direction = 6
                direction_détérminée = True

        #Logique pour déterminer la précision du tir d'aorès les paramètres et où le gardien va sauter
        if direction_détérminée and not saut_déterminé:
            # Fonction pour déterminer la précision, et les coordonées du mouvement
            précisions = Précision(flechedeprécision.précision, direction, sy, sx)
            sx = précisions[0]
            sy = précisions[1]
            Tir_précision = précisions[2]
            direction = précisions[3]
            # Fonction pour déterminer si la gardien va encaisser ou pas le ballon, et
            gardiensaut = sautgardien(flechedeforce.force, Tir_précision, direction)
            saut = gardiensaut[0]
            gardien.stop = gardiensaut[1]
            st = gardiensaut[2]
            player.run = True
            saut_déterminé = True



                #""""Application des valeurs calculées sur les classes"""

    # """Pour que le ballon ne sorte que lorsque le joueur chute le ballon"""
    if player.chutant == True:
        ballon.sx = sx
        ballon.sy = sy
        gardien.saut = [saut]


        ballon.speedy = ballon.sy * flechedeforce.force
        ballon.speedx = ballon.sx * flechedeforce.force
        print(Tir_précision)
        print(flechedeforce.force)
        print(st)
        print(gardien.saut)
        print(player.chutant)
        paramètres_appliqués = True

    # appliquer du son au jeu si on l'a habilité et compter le nombre de buts, de fois que le gardien a encaissé, et de tirs ratés, et aussi afficher l'image BUUUT
    if son:
        if paramètres_appliqués and ballon.stop and gardien.stop:
            if st == ["Bon"]:
                pygame.mixer.music.load(os.path.join(sound_folder, "tafarel.mp3"))
                pygame.mixer.music.play(0)
                pygame.time.delay(8000)
                gardien_pris += 1
            # pygame.time.delay(1000)
            if st == ["Mauvais"]:
                score += 1
                screen.blit(but, (200, 200))
                pygame.mixer.music.play(0)
                pygame.time.delay(3500)
                pygame.display.flip()
                pygame.time.delay(2000)

            if st == ["Immobile"] or st == ["PeuImporte"]:
                pygame.mixer.music.load(os.path.join(sound_folder, "errou.mp3"))
                pygame.mixer.music.play(0)
                isolé += 1

            tentatives += 1
            pygame.time.delay(2000)
            reiniciar = True
        if st == ["Mauvais"] and player.chutant and sound:
            pygame.mixer.music.load(os.path.join(sound_folder, "gol_cut.mp3"))
            pygame.mixer.music.play(0)
            sound = False

    # ne pas appliquer du son, et compter le nombre de buts, de fois que le gardien a encaissé, et de tirs ratés, et aussi afficher l'image BUUUT
    if not son:
        if paramètres_appliqués and ballon.stop and gardien.stop:
            # pygame.time.delay(1000)
            if st == ["Bon"]:
                gardien_pris += 1
            if st == ["Mauvais"]:
                score += 1
                screen.blit(but, (200, 200))
                pygame.display.flip()
                pygame.time.delay(2000)
            if st == ["Immobile"] or st == ["PeuImporte"]:
                isolé += 1
            tentatives += 1
            pygame.time.delay(2000)
            reiniciar = True

    # pour diminuer la taille du ballon et simuler 3d, que si le ballon a déjà une vitesse et n'est pas arrêté
    if ballon.sx != 0 and not ballon.stop:
        ballon.diminuer(flechedeforce.force)

    # appelle les méthodes des classes des sprites, poour aprés les montrer sur l'écran
    gardien.animate()
    all_sprites.update()
    all_sprites.draw(screen)

    # Afficher les scores sur l'écran dépendant que l'on veut 5 tentatives ou inifinies
    if running and tentatives < 5 and not infini:
        draw_text(screen, "Score : " + str(score), 40, 900, 30)
        draw_text(screen, "Tentatives : " + str(tentatives), 40, 100, 30)

    if running and infini:
        draw_text(screen, "Score : " + str(score), 40, 900, 30)
        raté = gardien_pris + isolé
        draw_text(screen, "Ratées : " + str(raté), 40, 100, 30)

    pygame.display.flip()

pygame.quit()
