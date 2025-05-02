# this allows us to use code from 
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import*
from player import*
from asteroid import*
from asteroidsfield import*
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astreoids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (astreoids, updateable, drawable)
    AsteroidField.containers = (updateable)
    obstacles = AsteroidField()
    gamer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)

        for asteroid in astreoids:
            if asteroid.collision(gamer):
                print("Game over!")
                sys.exit()

        screen.fill(color="black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()

        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()  

