import pygame
from player import Player

class Sprites():
    def __init__(self, screen):
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(Player(240/2, 180/2))
        self.all_sprites_list.draw(screen)