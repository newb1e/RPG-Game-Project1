import pygame
from player import Player
from map import Walking_zone
import globals


class Sprites():
    def __init__(self):
        self.all_sprites_list = pygame.sprite.LayeredUpdates()
        self.all_sprites_list.add(Player(globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2))
        self.all_sprites_list.add(Walking_zone((99, 101, 99), 100, 100))
    
    
    
        
