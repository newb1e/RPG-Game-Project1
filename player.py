import pygame as pg
from utils import load_image
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    PLAYER_HEALTH = 100
    
    def __init__(self, x, y):
        super().__init__()
        
        self.image, self.rect = load_image("topdown_shooter/characters/1.png")
        self.rect.center = (x, y)
        # self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.health = self.PLAYER_HEALTH

    # def get_keys(self):
    #     self.rot_speed = 0
    #     self.vel = vec(0, 0)
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_LEFT] or keys[pg.K_a]:
    #         self.rot_speed = PLAYER_ROT_SPEED
    #     if keys[pg.K_RIGHT] or keys[pg.K_d]:
    #         self.rot_speed = -PLAYER_ROT_SPEED
    #     if keys[pg.K_UP] or keys[pg.K_w]:
    #         self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
    #     if keys[pg.K_DOWN] or keys[pg.K_s]:
    #         self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
    #     if keys[pg.K_SPACE]:
    #         self.shoot()

    # def shoot(self):
    #     now = pg.time.get_ticks()
    #     if now - self.last_shot > WEAPONS[self.weapon]['rate']:
    #         self.last_shot = now
    #         dir = vec(1, 0).rotate(-self.rot)
    #         pos = self.pos + BARREL_OFFSET.rotate(-self.rot)
    #         self.vel = vec(-WEAPONS[self.weapon]['kickback'], 0).rotate(-self.rot)
    #         for i in range(WEAPONS[self.weapon]['bullet_count']):
    #             spread = uniform(-WEAPONS[self.weapon]['spread'], WEAPONS[self.weapon]['spread'])
    #             Bullet(self.game, pos, dir.rotate(spread), WEAPONS[self.weapon]['damage'])
    #             snd = choice(self.game.weapon_sounds[self.weapon])
    #             if snd.get_num_channels() > 2:
    #                 snd.stop()
    #             snd.play()
    #         MuzzleFlash(self.game, pos)

    # def hit(self):
    #     self.damaged = True
    #     self.damage_alpha = chain(DAMAGE_ALPHA * 4)

    # def update(self):
    #     self.get_keys()
    #     self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
    #     self.image = pg.transform.rotate(self.game.player_img, self.rot)
    #     if self.damaged:
    #         try:
    #             self.image.fill((255, 255, 255, next(self.damage_alpha)), special_flags=pg.BLEND_RGBA_MULT)
    #         except:
    #             self.damaged = False
    #     self.rect = self.image.get_rect()
    #     self.rect.center = self.pos
    #     self.pos += self.vel * self.game.dt
    #     self.hit_rect.centerx = self.pos.x
    #     collide_with_walls(self, self.game.walls, 'x')
    #     self.hit_rect.centery = self.pos.y
    #     collide_with_walls(self, self.game.walls, 'y')
    #     self.rect.center = self.hit_rect.center

    # def add_health(self, amount):
    #     self.health += amount
    #     if self.health > PLAYER_HEALTH:
    #         self.health = PLAYER_HEALTH