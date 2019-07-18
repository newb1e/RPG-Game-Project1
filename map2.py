import pygame
import os
from utils import load_image
import random
import globals
from spritesheet import Spritesheet

class Map2(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        self.bg_image = pygame.image.load("assets/bg_test.png")
        self.bg_rect = self.bg_image.get_rect()
        self.map_size = (width, height) = self.bg_image.get_size()
        self.sprite_group = pygame.sprite.Group()
        self.create_artifacts()
        
    def draw_map(self, x, y):
        #self.bg_rect.move(self.bg_rect.x + x, self.bg_rect.y + y)
        print(x, y)
        print(self.bg_rect)
        self.bg_rect.x = self.bg_rect.x + x
        self.bg_rect.y = self.bg_rect.y + y
        self.screen.blit(self.bg_image, self.bg_rect)
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)
    
    def create_artifacts(self):
        
        for a in range(10):
            # rocks
            self.sprite_group.add(Artifact(self.map_size, "assets/map_tiles/Outdoors_15.png"))
            # stems
            self.sprite_group.add(Artifact(self.map_size, "assets/map_tiles/Outdoors_17.png"))
            # tree
            self.sprite_group.add(Artifact(self.map_size, "assets/spritesheet/props_tree.png"))
            
            
class Artifact(pygame.sprite.Sprite):
    def __init__(self, map_size, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        #self.rect.x = 50
        #self.rect.y = 50
        self.rect.x = random.randrange(0, map_size[0], 16)
        self.rect.y = random.randrange(0, map_size[1], 16)
    
    def add_artifact(image):
        artifact = Artifact(self.map)
        self.sprite_group.add    
    
    def create_artifacts():
        add_artifact("assets/map_tiles/Outdoors_15.png")
    
        
        
        
        
        
        
    