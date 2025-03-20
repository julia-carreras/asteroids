import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        # Main game loop
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                return

        # Take player's input
        player.update(dt) 
        
        # Clear and draw in screen (buffer)
        screen.fill((0, 0, 0)) 
        player.draw(screen)
    
        # Make everything visible to user
        pygame.display.flip()
            
        # Calculate dt for next frame
        delta_time = clock.tick(60)
        dt = delta_time / 1000


        


    print('''
    Starting Asteroids!
    Screen width: 1280
    Screen height: 720''')






if __name__ == "__main__":
    main()