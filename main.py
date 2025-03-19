import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
            pygame.Surface.fill(screen, (0, 0, 0), rect=None, special_flags=0)
            pygame.display.flip()



    print('''
    Starting Asteroids!
    Screen width: 1280
    Screen height: 720''')






if __name__ == "__main__":
    main()