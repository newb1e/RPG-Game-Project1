import pygame
import os
from utils import load_image
import random
import globals

class Map:
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    
    def __init__(self, screen):
        self.tile_size = 16
        self.screen = screen
        self.bg_image = load_image("bg_test.png")[0]
        self.draw_background(self.screen)
        self.draw_rocks(self.screen)
        pygame.display.flip()
        
    def draw_background(self,screen):
        #num_of_tiles = (self.SCREEN_HEIGHT+self.SCREEN_HEIGHT)/tile_size
        bg_image = load_image("map_tiles/Outdoors_04.png")[0]
        for row in range(int(globals.SCREEN_HEIGHT/self.tile_size)):
            for col in range(int(globals.SCREEN_WIDTH/self.tile_size)):
                screen.blit(bg_image, (col*self.tile_size,row*self.tile_size))
        
    def draw_rocks(self,screen):
        num_of_rocks = 20
        rock_image = load_image("map_tiles/Outdoors_15.png")[0]
        for item in range(num_of_rocks):
            rand_width = random.randrange(0,globals.SCREEN_WIDTH-self.tile_size,1)
            rand_height = random.randrange(0,globals.SCREEN_WIDTH-self.tile_size,1)
            screen.blit(rock_image, (rand_width,rand_height))
        