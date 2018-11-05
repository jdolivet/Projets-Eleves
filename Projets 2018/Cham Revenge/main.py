# First game
import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

# HUD functions


# initialize the game object

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.mixer.pre_init(22050, -16,1,4096)
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        # let the key be repeated
        pg.key.set_repeat(500,100)
        self.clock = pg.time.Clock()
        self.running = True
        
        self.draw_debug = False
        self.paused = False
        self.night = False
        self.wingame = False
        self.change_level = False
        self.level_now = 'level1'

        self.draw_piece1 = False
        self.player_health_before = 0
        self.player_weapon_before = 0
        self.player_mag_before = 0
        self.bosspieces = 0
        self.coins = 2
        self.powerup = False

    def draw_player_health(self, surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_pieces(self, x, y, img):
        self.screen.blit(img,(x,y))


    def draw_text(self, text, font_name, size, color, x, y, align="nw"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def mini_load(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.title_font = path.join(img_folder, 'ZOMBIE.TTF')
        self.hud_font = path.join(img_folder, 'Impacted2.0.ttf')

    def load_player(self):
        self.player.weapon = self.player_weapon_before
        self.player.health = self.player_health_before
        self.player.bullet_left = self.player_mag_before

    def save_player(self):
        self.player_weapon_before = self.player.weapon
        self.player_health_before = self.player.health
        self.player_mag_before = self.player.bullet_left

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        map_folder = path.join(game_folder, 'maps')

        self.map_folder = path.join(game_folder, 'maps')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))

        self.map = TiledMap(path.join(map_folder, ALL_LEVELS[self.level_now]['map']))

        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.boss_img = pg.image.load(path.join(img_folder, BOSS_IMG)).convert_alpha()
        self.boss_img=pg.transform.scale(self.boss_img, (500, 500))


        self.bullet_img = {}
        self.bullet_img['lg'] =  pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_img['sm'] =  pg.transform.scale(self.bullet_img['lg'], (25,25))

        self.splat = pg.image.load(path.join(img_folder, SPLAT)).convert_alpha()
        self.splat = pg.transform.scale(self.splat, (64, 64))

        # lightning effects
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()

        self.powerup_img = pg.image.load(path.join(img_folder, POWERUP)).convert_alpha()

        self.gun_flashes = []
        for img in MUZZLE_FLASHES:
            self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())

        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()

        # sound loading
        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
        self.effects_sounds = {}
        for type in EFFECT_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECT_SOUNDS[type]))

        self.weapon_sounds = {}
        for weapon in WEAPON_SOUNDS:
            self.weapon_sounds[weapon]=[]
            for snd in WEAPON_SOUNDS[weapon]:
                s = pg.mixer.Sound(path.join(snd_folder, snd))
                s.set_volume(0.3)
                self.weapon_sounds[weapon].append(s)

        self.zombie_moan_sounds = []
        for snd in ZOMBIE_MOAN_SOUNDS:
            s = pg.mixer.Sound(path.join(snd_folder, snd))
            s.set_volume(0.02)
            self.zombie_moan_sounds.append(s)

        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUNDS:
            self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))

        self.zombie_hit_sounds = []
        for snd in ZOMBIE_HIT_SOUNDS:
            self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))


        #self.bullet_img = pg.transform.scale(self.bullet_img, (10, 10))

    def new(self):
        self.load_data()
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.machines = pg.sprite.LayeredUpdates()
        self.safezones = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.LayeredUpdates()
        self.mobs = pg.sprite.LayeredUpdates()
        self.bullets = pg.sprite.LayeredUpdates()
        self.items = pg.sprite.LayeredUpdates()
        self.door = pg.sprite.LayeredUpdates()

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x +tile_object.width / 2, tile_object.y +tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
                if self.change_level == True:
                    self.load_player()
                    self.change_level = False
            if tile_object.name == 'wall':
                Obstacles(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'safe':
                Safe_zone(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'zombie':
                Mob(self, tile_object.x, tile_object.y)
            if tile_object.name == 'boss':
                Boss(self, tile_object.x, tile_object.y)
            if tile_object.name in ['health', 'shotgun', 'talisman1']:
                Item(self, obj_center, tile_object.name)
            if tile_object.name == 'machine':
                Machine(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name == 'door':
                Door(self, tile_object.x, tile_object.y,tile_object.width, tile_object.height)

        self.camera = Camera(self.map.width, self.map.height)
        self.effects_sounds['level_start'].play()


        self.run()


    def run(self):
        self.playing = True
        pg.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)


        # game over
        if len(self.mobs) == 0 and self.wingame == True:
            self.playing = False
            self.draw_piece1 = False
            self.powerup = False
            self.level_now = 'level1'
            self.show_go_screen()


        # player hits items
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.add_health(HEALTH_PACK_AMMOUNT)
            if hit.type == 'shotgun':
                hit.kill()
                self.player.bullet_left = WEAPONS['shotgun']['mag_size']
                self.effects_sounds['gun_pickup'].play()
                self.player.weapon='shotgun'
            if hit.type == 'talisman1':
                hit.kill()
                self.bosspieces += 1
                self.draw_piece1 = True


        # mobs hitting player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            if random() <0.7:
                choice(self.player_hit_sounds).play()
            hit.vel = vec(0,0)
            if self.player.health <=0:
                self.playing = False
                self.powerup = False
                self.draw_piece1 = False
                self.show_go_screen()
        if hits:
            self.player.hit()
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)

        # bullets hits mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for mob in hits:
            for bullet in hits[mob]:
                mob.health -= bullet.damage
            mob.vel = vec(0,0)

        hit = pg.sprite.spritecollide(self.player, self.door, False, collide_wall)
        if hit and self.bosspieces == 1:
            self.playing = False
            self.change_level = True
            self.level_now = 'boss'
            self.save_player()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night

    def render_fog(self):
        # draw light mask onto fog image
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0,0), special_flags = pg.BLEND_MULT)

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))

            if isinstance(sprite, Mob) or isinstance(sprite, Player) or isinstance(sprite, Bullet) or isinstance(sprite, Boss):
                if self.draw_debug:
                    pg.draw.rect(self.screen, RED, self.camera.apply_rect(sprite.hit_rect), 1)

        if self.night:
            self.render_fog()



        # HUD functions
        if self.draw_piece1 == True:
            self.draw_pieces(5, 15, self.item_images['talisman1'])

        if self.powerup == True:
            self.screen.blit(self.powerup_img, (WIDTH / 2, 5))

        self.draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_text('Zombies: {}'.format(len(self.mobs)), self.hud_font, 30, WHITE, WIDTH - 10, 10, align ='ne')
        self.draw_text('Coins: {}'.format(self.coins), self.hud_font, 30, YELLOW, WIDTH - 10, 40, align ='ne')
        self.draw_text('Bullets: {}'.format(self.player.bullet_left), self.hud_font, 30, BLUE, WIDTH - 10, 70, align ='ne')
        if self.paused:
            self.screen.blit(self.dim_screen, (0,0))
            self.draw_text("Paused", self.title_font, 105, RED, WIDTH /2, HEIGHT /2, "center")
        pg.display.flip()

    def show_start_screen(self):
        self.mini_load()
        self.screen.fill(BLACK)
        self.draw_text("Press a key to start ICI", self.title_font, 75, WHITE, WIDTH / 2, HEIGHT *3/4, align='center')
        pg.display.flip()
        self.wait_for_key()
        pass

    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, RED, WIDTH / 2, HEIGHT /2, align='center')
        self.draw_text("Press a key to start", self.title_font, 75, WHITE, WIDTH / 2, HEIGHT *3/4, align='center')
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False



g = Game()
g.show_start_screen()
while g.running:
    g.new()

pg.quit()