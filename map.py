import pygame
import os
from utils import load_image
import random
import globals
from spritesheet import Spritesheet


class Map:
    global SCREEN_WIDTH
    global SCREEN_HEIGHT

    def __init__(self, screen):
        self.tile_size = 16
        self.screen = screen
        self.bg_image = load_image("bg_test.png")[0]
        self.ss = Spritesheet("assets/spritesheet/tileset_florest.png")
        self.draw_background(self.screen)
        
        self.draw_tile(self.screen, "map_tiles/Outdoors_15.png",10)  # Draw rocks
        self.draw_tile(self.screen, "map_tiles/Outdoors_17.png",12)  # Draw stems
        self.draw_tile(self.screen, "spritesheet/props_tree.png", 5)
        self.draw_tile(self.screen, "spritesheet/props_tree_goup.png", 3)
        self.draw_tile(self.screen, "spritesheet/props_skull.png", 4)
        self.draw_tile(self.screen, "spritesheet/props_grasschest_closed.png", 4)
        
        self.player_walking_radius(self.screen, 60)
        pygame.display.flip()
    """    
    def draw_background(self,screen):
        bg_image = load_image("map_tiles/Outdoors_04.png")[0]
        for row in range(int(globals.SCREEN_HEIGHT/self.tile_size)):
            for col in range(int(globals.SCREEN_WIDTH/self.tile_size)):
                screen.blit(bg_image, (col*self.tile_size,row*self.tile_size))
    """

    def draw_background(self, screen):
        bg_image = self.ss.image_at((53, 0, 16, 16))
        for row in range(int(globals.SCREEN_HEIGHT/self.tile_size)):
            for col in range(int(globals.SCREEN_WIDTH/self.tile_size)):
                screen.blit(bg_image, (col*self.tile_size, row*self.tile_size))

    def draw_tile(self, screen, image, num_of_tiles):
        num_of_stems = 10
        tile_image = load_image(image)[0]
        if "spritesheet" in image:
            tile_image.set_colorkey((99, 101, 99))
        else:
            tile_image.set_colorkey((0, 0, 0))
        for item in range(num_of_tiles):
            rand_width = random.randrange(0, globals.SCREEN_WIDTH-64, 16)
            rand_height = random.randrange(0, globals.SCREEN_HEIGHT-64, 16)
            screen.blit(tile_image, (rand_width, rand_height))

    def player_walking_radius(self, screen, radius):
        circle_location = (int(globals.SCREEN_WIDTH/2),int(globals.SCREEN_HEIGHT/2))
        surface = pygame.Surface((globals.SCREEN_WIDTH,globals.SCREEN_HEIGHT), pygame.SRCALPHA)
        circle = pygame.draw.circle(surface, (99, 101, 99,128), circle_location, radius)
        screen.blit(surface, (0,0))
        


class Camera:
    
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    
        
