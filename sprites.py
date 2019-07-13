import pygame
from player import Player
import globals

class Sprites():
    def __init__(self):
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(Player(globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2))