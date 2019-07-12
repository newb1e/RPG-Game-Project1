import pygame
import os
from utils import load_image
import random
import globals

class spritesheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print ('Unable to load spritesheet image:', filename)
            raise SystemExit(message)
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)

class Map:
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    
    def __init__(self, screen):
        self.tile_size = 16
        self.screen = screen
        self.bg_image = load_image("bg_test.png")[0]
        self.ss = spritesheet("assets/spritesheet/tileset_florest.png")
        self.draw_backgroundii(self.screen)
        self.draw_rocks(self.screen)
        pygame.display.flip()
    """    
    def draw_background(self,screen):
        bg_image = load_image("map_tiles/Outdoors_04.png")[0]
        for row in range(int(globals.SCREEN_HEIGHT/self.tile_size)):
            for col in range(int(globals.SCREEN_WIDTH/self.tile_size)):
                screen.blit(bg_image, (col*self.tile_size,row*self.tile_size))
    """   
    def draw_backgroundii(self,screen):
        bg_image = self.ss.image_at((0, 0, 16, 16))
        for row in range(int(self.SCREEN_HEIGHT/self.tile_size)):
            for col in range(int(self.SCREEN_WIDTH/self.tile_size)):
                screen.blit(bg_image, (col*self.tile_size,row*self.tile_size))
        
    
    def draw_rocks(self,screen):
        num_of_rocks = 20
        rock_image = load_image("spritesheet/props_big_stone.png")[0]
        for item in range(num_of_rocks):
            rand_width = random.randrange(0,globals.SCREEN_WIDTH-self.tile_size,1)
            rand_height = random.randrange(0,globals.SCREEN_WIDTH-self.tile_size,1)
            screen.blit(rock_image, (rand_width,rand_height))
            rock_image.set_alpha(None)
            rock_image.set_colorkey((255,0,255))
        