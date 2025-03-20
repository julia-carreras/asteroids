import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
            screen.fill((0, 0, 0))
            player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            player.draw(screen)
            pygame.display.flip()
            
            delta_time = clock.tick(60)
            dt = delta_time / 1000


        


    print('''
    Starting Asteroids!
    Screen width: 1280
    Screen height: 720''')






if __name__ == "__main__":
    main()