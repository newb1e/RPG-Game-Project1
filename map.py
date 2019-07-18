import pygame
import os
from utils import load_image
import random
import globals
from spritesheet import Spritesheet


class Map:
    def __init__(self,screen):
        self.screen = screen
        self.width = globals.MAP_WIDTH
        self.height = globals.MAP_HEIGHT
        self.x = 0
        self.y = 0 
        self.screen_width = globals.SCREEN_WIDTH
        self.screen_height = globals.SCREEN_HEIGHT
        self.tile_size = 16
        self.map_surface = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
        self.ss = Spritesheet("assets/spritesheet/tileset_florest.png")
        self.draw_background(self.map_surface)
        
        self.draw_tile(self.map_surface, "map_tiles/Outdoors_15.png",10)  # Draw rocks
        self.draw_tile(self.map_surface, "map_tiles/Outdoors_17.png",12)  # Draw stems
        self.draw_tile(self.map_surface, "spritesheet/props_tree.png", 5)
        self.draw_tile(self.map_surface, "spritesheet/props_tree_goup.png", 3)
        self.draw_tile(self.map_surface, "spritesheet/props_skull.png", 4)
        self.draw_tile(self.map_surface, "spritesheet/props_grasschest_closed.png", 4)
        
        #self.player_walking_radius(self.screen, 60)
        #return self.map_surface
        #screen.blit(self.map_surface,(100,100))
        #pygame.display.flip()
        
    def get_map(self):
        return self.map_surface

    def draw_background(self, map_surface):
        bg_image = self.ss.image_at((53, 0, 16, 16))
        for row in range(int(self.height/self.tile_size)):
            for col in range(int(self.width/self.tile_size)):
                map_surface.blit(bg_image, (col*self.tile_size, row*self.tile_size))

    def draw_tile(self, map_surface, image, num_of_tiles):
        num_of_stems = 10
        tile_image = load_image(image)[0]
        if "spritesheet" in image:
            tile_image.set_colorkey((99, 101, 99))
        else:
            tile_image.set_colorkey((0, 0, 0))
        for item in range(num_of_tiles):
            rand_width = random.randrange(0, self.width-64, 16)
            rand_height = random.randrange(0, self.height-64, 16)
            map_surface.blit(tile_image, (rand_width, rand_height))
            
    def move_map(self, direction, speed):
        
            self.map_surface.blit(self.get_map(),(self.x+speed,self.y+speed))
"""
    def player_walking_radius(self, radius):
        circle_location = (int(self.screen_width/2),int(self.screen_height/2))
        surface = pygame.Surface((self.screen_width,self.screen_height), pygame.SRCALPHA)
        circle = pygame.draw.circle(surface, (99, 101, 99,128), circle_location, radius)
        #rect = pygame.Rect()
        return surface
"""
  
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

        


class Camera:
    
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.pos_x = int(width/2)
        self.pos_y = int(height/2)
        
    def move(self, move_x, move_y):
        self.pos_x += move_x 
        self.pos_y += move_y
    
    
        
