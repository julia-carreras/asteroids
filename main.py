import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # Link to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    
    # Create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    
    while True:
        # Main game loop
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                return
        
        # Take player's input
        updatable.update(dt) 
        
        # Clear and draw in screen (buffer)
        screen.fill((0, 0, 0)) 
        for obj in drawable:
            obj.draw(screen)
    
        # Make everything visible to user
        pygame.display.flip()
            
        # Calculate dt for next frame
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()