# import the pygame module, so you can use it
import pygame
import os
from sprites import Sprites
from utils import load_image
from map import *
import globals
 
# define a main function
def main():
    globals.init()
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load(os.path.join("assets/topdown_shooter/characters/","1.png"))
    pygame.display.set_icon(logo)   
    pygame.display.set_caption("minimal program")
    
    screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT), 0, 16)
    
    # create instance of Map and draw the map
    game_map = Map(screen)
    sprites = Sprites()
    
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1, 40)
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            sprites.all_sprites_list.draw(screen)s
            sprites.all_sprites_list.update()
            
            pygame.display.flip()
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()