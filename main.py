import pygame
import os
from utils import load_image
from map import *
from player import *
import globals
 
class Game():
    def __init__(self):
        pygame.key.set_repeat(1, globals.KEY_REPEAT)
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT), 0, 16)
        self.map = Map(self.screen)
        self.player = Player(globals.SCREEN_WIDTH/2, globals.SCREEN_HEIGHT/2)
        self.all_sprites_list = pygame.sprite.LayeredUpdates()
        self.all_sprites_list.add(self.player)
        
    def run_game(self):
        running = True
        
        while running:
            self.map.draw_map(0, 0)
            
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                
                if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                    self.map.draw_map(globals.PLAYER_SPEED, 0)
                    
                if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                    self.map.draw_map(-globals.PLAYER_SPEED, 0)
                    
                if keys[pygame.K_UP] or keys[pygame.K_w]:
                    self.map.draw_map(0, globals.PLAYER_SPEED)    
                    
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.map.draw_map(0, -globals.PLAYER_SPEED)
            
                self.all_sprites_list.draw(self.screen)
                self.all_sprites_list.update()
                
                pygame.display.flip()
                
                if event.type == pygame.QUIT:
                    running = False
                    
    def move_game():
        return
        
def main():
    pygame.init()
    globals.init()
    set_logo()
    game = Game()
    game.run_game()
     
def set_logo():
    logo = pygame.image.load(os.path.join("assets/topdown_shooter/characters/","1.png"))
    pygame.display.set_icon(logo)   
    pygame.display.set_caption("minimal program")
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    main()