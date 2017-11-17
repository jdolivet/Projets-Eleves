import pygame
import math



def nouvelle_cord(sprite, direction, objetcollision, ajoutx, ajouty,cordB):

    ### fonction qui retourne une liste avec deux coordonnées en fonction de l'hauteur ou la largeur du sprite lors d'une collision
    nouvellescord=[]

    cord_inter1 = (sprite.rect.x, sprite.rect.y)
    cord_inter2 = 0#coordonnée avant l'obstacle, qui sera utilisée lors du déplacement

    if direction =='x':
        if ajoutx>0:    #se déplace vers la droite
            x2=sprite.rect.x+sprite.rect.width+objetcollision[0].rect.width
            if cordB[0]<x2:
                pass
            else:
                sprite.rect.x = x2                #on crée une deuxième coordonnée après l'obstacle
                cord_inter2 = (x2, sprite.rect.y)
        elif ajoutx<0:
            x2 = sprite.rect.x - sprite.rect.width - objetcollision[0].rect.width
            if cordB[0]>x2:
                pass
            else:
                sprite.rect.x = x2
                cord_inter2 = (x2, sprite.rect.y)
    elif direction =='y':
        if ajouty>0:
            y2 = sprite.rect.y+sprite.rect.height+objetcollision[0].rect.height
            if cordB[1] < y2:
                pass
            else:
                cord_inter2 = (sprite.rect.x, y2)
        elif ajouty<0:
            y2=sprite.rect.y-sprite.rect.height-objetcollision[0].rect.height
            if cordB[1] > y2:
                pass
            else:
                cord_inter2 = (sprite.rect.x, y2)


    if pygame.sprite.spritecollide(sprite,sprite.game.obstacles_sprites, False):
        return False
    else:
        if cord_inter2!=0:
            nouvellescord = [cord_inter1,cord_inter2]
        else:
            nouvellescord = [cord_inter1]


        return nouvellescord

def choisir_chemin(liste_chemins):

    ancienne_cord =0
    distance =0
    chemin_plus_court = 0
    ancienne_distance = 0
    d = {}
    for chemin in liste_chemins:
        nb=0
        distance = 0
        for cord in chemin[1:]:
            distance += math.sqrt((cord[0]-chemin[nb][0])**2 + (cord[1]-chemin[nb][1])**2)
            nb+=1
        d[distance]=chemin
    print(d)


    for distance in d:
        if distance < ancienne_distance and ancienne_distance !=0:
            ancienne_distance = distance
            chemin_plus_court= d[distance]
        elif ancienne_distance == 0:
            ancienne_distance = distance
            chemin_plus_court = d[distance]

    print(chemin_plus_court)
    return chemin_plus_court


def testmouvement(sprite_obj, cordB):
    ajoutx = 0
    ajouty = 0
    x = sprite_obj.rect.x
    y = sprite_obj.rect.y
    chemins_possibles = [[(x,y),cordB]]
    chemins_réalisables = []
    for chemin in chemins_possibles:
        if len(chemin)>1:
            sprite_obj.rect.x = chemin[len(chemin)-2][0] #attribue a rect.x la valeur de x de l'avant dernière coordonée
            sprite_obj.rect.y = chemin[len(chemin)-2][1]# de meme pour y
        if len(chemins_réalisables)>5:
            break
        print(chemins_possibles)


        while (abs(cordB[1] - sprite_obj.rect.y)) >= 1 or (abs(cordB[0] - sprite_obj.rect.x)) >= 1:     #tant que le sprite n'est pas à CordB

            ajoutx = 0
            ajouty = 0

            if cordB[0] > sprite_obj.rect.x:                #mouvement x
                ajoutx = 1
            elif cordB[0] < sprite_obj.rect.x:
                ajoutx = -1
            sprite_obj.rect.x += ajoutx


            objetcollision = pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites, False)

            if objetcollision:
                xbackup = sprite_obj.rect.x
                sprite_obj.rect.y = objetcollision[0].rect.y + objetcollision[0].rect.height
                if pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites, False):
                    pass
                else:
                    cord_inter = nouvelle_cord(sprite_obj, 'x', objetcollision, ajoutx, ajouty,cordB)
                    if cord_inter == False:
                        pass

                    else:
                        chemin_nouveau2 = chemin[0:len(chemin)-1] + cord_inter + chemin[len(chemin)-1:len(chemin)]
                        chemins_possibles.append(chemin_nouveau2)

                sprite_obj.rect.x = xbackup
                sprite_obj.rect.y = objetcollision[0].rect.y - sprite_obj.rect.height

                if pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites, False):
                    pass
                else:
                    cord_inter = nouvelle_cord(sprite_obj,'x', objetcollision, ajoutx, ajouty,cordB)
                    if cord_inter == False:
                        break
                    else:
                        chemin_nouveau2 = chemin[0:len(chemin)-1] + cord_inter + chemin[len(chemin)-1:len(chemin)]
                        chemins_possibles.append(chemin_nouveau2)

                break



            if cordB[1] > sprite_obj.rect.y:                #mouvement y
                ajouty = 1
                sprite_obj.image = sprite_obj.imagedevant
            elif cordB[1] < sprite_obj.rect.y:
                ajouty = -1
                sprite_obj.image = sprite_obj.imagederriere
            sprite_obj.rect.y += ajouty




            objetcollision = pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites, False)

            if objetcollision:

                ybackup = sprite_obj.rect.y
                sprite_obj.rect.x = objetcollision[0].rect.x + objetcollision[0].rect.width + 1
                if pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites,False) or sprite_obj.rect.x >= 2434:
                    pass
                else:
                    cord_inter = nouvelle_cord(sprite_obj, 'y', objetcollision, ajoutx, ajouty,cordB)
                    chemin_nouveau = chemin[0:len(chemin)-1] + cord_inter + chemin[len(chemin)-1:len(chemin)]
                    chemins_possibles.append(chemin_nouveau)



                sprite_obj.rect.y = ybackup
                sprite_obj.rect.x = objetcollision[0].rect.x - sprite_obj.rect.width - 1

                # test collision côté gauche
                if pygame.sprite.spritecollide(sprite_obj, sprite_obj.game.obstacles_sprites, False):
                    pass

                else:
                    cord_inter = nouvelle_cord(sprite_obj,'y', objetcollision, ajoutx, ajouty,cordB)
                    chemin_nouveau2 = chemin[0:len(chemin)-1] + cord_inter + chemin[len(chemin)-1:len(chemin)]
                    chemins_possibles.append(chemin_nouveau2)

                break



        if (abs(cordB[1] - sprite_obj.rect.y)) <= 1 and (abs(cordB[0] - sprite_obj.rect.x)) <= 1:
            chemins_réalisables.append(chemin)





    liste_cord=choisir_chemin(chemins_réalisables)
    print(sprite_obj.rect)
    sprite_obj.rect.x = x
    sprite_obj.rect.y = y
    return liste_cord
