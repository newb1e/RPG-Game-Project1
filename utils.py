import os
import pygame

def load_image(name):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print ('Cannot load image:', fullname)
        raise SystemExit(message)
    image = image.convert()
   
    return image, image.get_rect()