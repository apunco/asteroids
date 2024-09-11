# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from powerup.powerup import PowerUp
from powerup.powerupenum import *
from powerup.powerupui import PowerUpUi
from screendimensions.screendimensions import *
from screendimensions.screencoordinatesenum import *

def main():
    pygame.init()
    set_screen_dimensions(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode((screendimensions[ScreenDimensionsEnum.WIDTH], screendimensions[ScreenDimensionsEnum.HEIGHT]))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    PowerUp.containers = (powerups, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    PowerUpUi.containers = (drawable, updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.VIDEORESIZE or event.type == pygame.VIDEOEXPOSE:
                screensize = screen.get_size()
                set_screen_dimensions(screensize[0], screensize[1])

        screen.fill("black")

        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                #sys.exit()
            
            asteroid.check_border_collision()
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.collide()
                    asteroid.split()                
            
        for powerup in powerups:
            if powerup.check_collision(player):
                player.get_powerup(powerup)

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

def set_screen_dimensions(width, height):
    screendimensions[ScreenDimensionsEnum.WIDTH] = width + BORDER_RIGHT_OFFSET + BORDER_LEFT_OFFSET
    screendimensions[ScreenDimensionsEnum.HEIGHT] = height + BORDER_TOP_OFFSET + BORDER_BOTTOM_OFFSET

    screencoordinates[ScreenCoordinatesEnum.LEFT] = BORDER_LEFT_OFFSET
    screencoordinates[ScreenCoordinatesEnum.RIGHT] = screendimensions[ScreenDimensionsEnum.WIDTH] - BORDER_RIGHT_OFFSET - BORDER_LEFT_OFFSET - SCREEN_BORDER_WIDTH * 2
    screencoordinates[ScreenCoordinatesEnum.TOP] = BORDER_TOP_OFFSET
    screencoordinates[ScreenCoordinatesEnum.BOTTOM] = screendimensions[ScreenDimensionsEnum.HEIGHT] - BORDER_BOTTOM_OFFSET - screencoordinates[ScreenCoordinatesEnum.TOP] - SCREEN_BORDER_WIDTH * 2
    
    print(screendimensions)
    print(screencoordinates)

if __name__ == "__main__":
    main()




