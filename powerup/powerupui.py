import pygame
from screendimensions.screendimensions import *
from screendimensions.screencoordinatesenum import *
from shape import Shape

class PowerUpUi(Shape):
    def __init__(self):
        super().__init__(0, 0, 0)

        self.position = pygame.Vector2(0, 0)
        self.powerups = {}

    def draw(self, screen):
        pygame.draw.rect(screen, "BLACK", pygame.Rect(0, 
                                                      screendimensions[ScreenDimensionsEnum.HEIGHT],
                                                      screendimensions[ScreenDimensionsEnum.WIDTH] / 3), 
                                                      screendimensions[ScreenDimensionsEnum.HEIGHT] - screencoordinates[ScreenCoordinatesEnum.TOP],
                                                      5)

    def update(self, dt):
        pass

    def add_powerup(self, powerup):
        pass
