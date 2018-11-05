import pygame as pg
import pytmx
from settings2t import *

###CLASS DE LA MAP 
class TiledMap:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth##NOMBRE DE PIXEL PAR TILED*NOMBRE DE TILED
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft) # retourne rectangle player deplacer par (x,y) de la camerara 

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft) ## retourne rectangle de la map deplacer par (x,y) de la camera

    def update(self, target):
        #print("update camera")
        x = -target.rect.centerx + int(LARGEUR / 2)
        y = -target.rect.centery + int(HAUTEUR / 2)
        #print(x,y)
        # limite du déroulaé to map size
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(-(self.width - LARGEUR), x)  # right
        y = max(-(self.height - HAUTEUR), y)  # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)
