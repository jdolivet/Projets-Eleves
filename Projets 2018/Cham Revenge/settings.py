# game options and settings
import os
import pygame as pg
vec = pg.math.Vector2

# game settings
TITLE = "Tilemap Demo"
WIDTH = 1024  # 32 *32
HEIGHT = 768  # 32 * 24
FPS = 60
FONT_NAME ='arial'

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WALL_IMG = 'tile_180.png'

# Players settings

PLAYER_HEALTH = 100
PLAYER_SPEED = 400
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
BARREL_OFFSET = vec(30, 10)

# Weapon settings

WEAPONS = {}

WEAPONS['pistol'] = {'bullet_speed': 500,
                     'bullet_lifetime' : 2000,
                     'bullet_rate': 150,
                     'rate': 250,
                     'kickback': 200,
                     'spread': 5,
                     'damage': 10,
                     'mag_size': 12,
                     'bullet_size': 'lg',
                     'bullet_count': 1}

WEAPONS['shotgun'] = {'bullet_speed': 400,
                     'bullet_lifetime' : 700,
                     'rate': 200,
                     'kickback': 300,
                     'spread': 10,
                     'damage': 5,
                     'mag_size':50,
                     'bullet_size': 'sm',
                     'bullet_count': 10}

BULLET_IMG = 'tile_187.png'


# Mob settings

MOB_IMG = 'zoimbie1_hold.png'
BOSS_IMG = 'zombie_boss.png'
MOB_SPEEDS = [150, 100, 75, 125, 20]
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 5
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
BOSS_HIT_RECT = pg.Rect(0, 0, 400, 400)
AVOID_RADIUS = 50
DETECT_RADIUS = 400

# Effects

MUZZLE_FLASHES = ['whitePuff15.png','whitePuff16.png','whitePuff17.png','whitePuff18.png']
FLASH_DURATION = 40
SPLAT = 'splat green.png'
DAMAGE_ALPHA = [i for i in range(0, 255, 55)]
NIGHT_COLOR = (5, 5, 5)
LIGHT_RADIUS = (500,500)
LIGHT_MASK = 'light_350_med.png'
POWERUP = 'powerup.png'

# Layers

WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEMS_LAYER = 1

# items
ITEM_IMAGES = {'health': 'health_pack.png',
               'shotgun': 'obj_shotgun.png',
               'talisman1': 'talis_1.png'}
HEALTH_PACK_AMMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.3


#Sounds
BG_MUSIC = 'espionage.ogg'
PLAYER_HIT_SOUNDS = ['pain/8.wav', 'pain/11.wav', 'pain/10.wav', 'pain/11.wav']
ZOMBIE_MOAN_SOUNDS = ['brains2.wav', 'brains3.wav', 'zombie-roar-1.wav', 'zombie-roar-2.wav',
                      'zombie-roar-3.wav', 'zombie-roar-4.wav', 'zombie-roar-5.wav',
                      'zombie-roar-6.wav', 'zombie-roar-7.wav']
ZOMBIE_HIT_SOUNDS = ['splat-15.wav']
WEAPON_SOUNDS = {'pistol': ['pistol.wav'],
                     'shotgun' : ['shotgun.wav'],
                    'reload' : ['reload.wav']}
EFFECT_SOUNDS = {'level_start': 'level_start.wav',
                 'health_up': 'health_pack.wav',
                 'gun_pickup': 'gun_pickup.wav'}

# All levels

ALL_LEVELS={}
ALL_LEVELS['level1']={'map': 'level1.tmx'}
ALL_LEVELS['level2']={'map': 'level2.tmx'}
ALL_LEVELS['level3']={'map': 'level3.tmx'}
ALL_LEVELS['level4']={'map': 'level4.tmx'}
ALL_LEVELS['boss']={'map': 'boss.tmx'}
