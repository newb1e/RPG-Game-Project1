import pygame
import spritesheet
import globals
from utils import load_image
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    PLAYER_HEALTH = 100
    PLAYER_ROT_SPEED = 200
    PLAYER_IMAGE_PATH = "topdown_shooter/characters"
    PLAYER_IMAGE_NORTH = "1_north.png"
    PLAYER_IMAGE_SIDE = "1_side.png"
    PLAYER_IMAGE_SOUTH = "1_south2.png"

    def __init__(self, x, y):
        super().__init__()

        self.image, self.rect = load_image(self.PLAYER_IMAGE_PATH + "/1.png")
        # self.spritesheet = spritesheet.spriteshee('somespritesheet.png')
        self.rect.center = (x, y)
        self.vel = vec(0, 0)
        self.rot = 0
        self.pos = vec(x, y)
        self.health = self.PLAYER_HEALTH
        self.walking_zone = Walking_zone((99, 101, 99), 100, 100)

    def get_keys(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos = vec(self.pos.x - self.PLAYER_SPEED, self.pos.y)
            
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
             self.pos = vec(self.pos.x + self.PLAYER_SPEED, self.pos.y)
             
        if keys[pygame.K_UP] or keys[pygame.K_w]:
             self.pos = vec(self.pos.x, self.pos.y - self.PLAYER_SPEED)
             
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
           self.pos = vec(self.pos.x, self.pos.y + self.PLAYER_SPEED)
            # self.shoot()

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

    def get_sprite_sheet():
       
        # Sprite is 16x16 pixels at location 0,0 in the file...
        image = ss.image_at((0, 0, 16, 16))
        images = []
        # Load two images into an array, their transparent bit is (255, 255, 255)
        images = ss.images_at((0, 0, 16, 16), (17, 0, 16, 16),
                            colorkey=(255, 255, 255))

    def update(self):
        #self.get_keys()
        # self.rot = (self.rot + self.rot_speed) % 360  # * self.game.dt
        # self.image = pg.transform.rotate(self.image, self.rot)
        # if self.damaged:
        #     try:
        #         self.image.fill((255, 255, 255, next(self.damage_alpha)), special_flags=pg.BLEND_RGBA_MULT)
        #     except:
        #         self.damaged = False
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        # self.pos += self.vel  # * self.game.dt
        # self.hit_rect.centerx = self.pos.x
        # collide_with_walls(self, self.game.walls, 'x')
        # self.hit_rect.centery = self.pos.y
        # collide_with_walls(self, self.game.walls, 'y')
        # self.rect.center = self.hit_rect.center

        # def add_health(self, amount):
        #     self.health += amount
        #     if self.health > PLAYER_HEALTH:
        #         self.health = PLAYER_HEALTH


class Walking_zone(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height):
        rect_position = (int((globals.SCREEN_WIDTH/2)-width/2),int((globals.SCREEN_HEIGHT/2)-height/2))
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.set_alpha(128)
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x = rect_position[0] 
        self.rect.y = rect_position[1]
        