import pygame
import os
from utils import load_image
import random
import globals
from spritesheet import Spritesheet

class Map():
    def __init__(self,screen):
        self.screen = screen
        self.bg_image = pygame.image.load("assets/bg_test.png")
        self.bg_rect = self.bg_image.get_rect()
        self.map_size = (width, height) = self.bg_image.get_size()
        self.map_artifacts = pygame.sprite.Group()
        self.create_artifacts()
        
    def draw_map(self, x, y):
        self.move_map(x, y)
        self.screen.blit(self.bg_image, self.bg_rect)
        self.map_artifacts.draw(self.screen)
    
    def move_map(self, x, y):
        border = (globals.SCREEN_WIDTH - self.bg_rect.width, globals.SCREEN_HEIGHT - self.bg_rect.height)
        
        if  self.bg_rect.x + x <= 0 and self.bg_rect.x + x >= border[0]:
            self.bg_rect.x = self.bg_rect.x + x
            self.move_artifacts(x, 0)
        #else
            #move player
        if  self.bg_rect.y + y <= 0 and self.bg_rect.y + y >= border[1]:
            self.bg_rect.y = self.bg_rect.y + y
            self.move_artifacts(0, y)
        #else
            #move player
            
    def move_artifacts(self, x, y):
        for artifact in self.map_artifacts:
            artifact.move(x, y)
    
    def create_artifacts(self):
        for a in range(10):
            # rocks
            self.map_artifacts.add(Artifact(self.map_size, "assets/map_tiles/Outdoors_15.png"))
            # stems
            self.map_artifacts.add(Artifact(self.map_size, "assets/map_tiles/Outdoors_17.png"))
            # tree
            self.map_artifacts.add(Artifact(self.map_size, "assets/spritesheet/props_tree.png"))
            
            
class Artifact(pygame.sprite.Sprite):
    def __init__(self, map_size, image):
        super().__init__()
        
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, map_size[0], 16)
        self.rect.y = random.randrange(0, map_size[1], 16)
    
    def add_artifact(image):
        artifact = Artifact(self.map)
        self.sprite_group.add    
    
    def create_artifacts():
        add_artifact("assets/map_tiles/Outdoors_15.png")
    
    def move(self, x, y):
            self.rect.x += x
            self.rect.y += y
        
        
        
        
        
    