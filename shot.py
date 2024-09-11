from shape import Shape
from constants import *
from powerup.powerupenum import PowerUpEnum
from screendimensions.screendimensions import *
from screendimensions.screencoordinatesenum import *

import pygame
import random

class Shot(Shape):
    def __init__(self, x, y, mods):
        super().__init__(x, y, SHOT_RADIUS)
        self.mods = mods
        self.split = False

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self,dt):
        self.position += self.velocity * dt

        # Check for out of Bounds
        if ((self.position.x < screencoordinates[ScreenCoordinatesEnum.LEFT] or self.position.x > screencoordinates[ScreenCoordinatesEnum.RIGHT]) or
            (self.position.y < screencoordinates[ScreenCoordinatesEnum.TOP] or self.position.y > screencoordinates[ScreenCoordinatesEnum.BOTTOM])):
            self.kill()
            
    def collide(self):
        if len(self.mods) == 0:
            self.kill()
        
        # self.mods.sort(key=lambda x: x.type)
        list(self.mods).sort()
        undestrucible = PowerUpEnum.UNDESTRACTABLE.value in self.mods
        guided = PowerUpEnum.GUIDED.value in self.mods

        if PowerUpEnum.SPLIT_SHOT.value in self.mods and not self.split:
            self.split = True
            random_angle = random.uniform(10, 30)

            vector_one = self.velocity.rotate(random_angle)
            vector_two = self.velocity.rotate(-random_angle)

            shot_one = Shot(self.position.x, self.position.y, self.mods)
            shot_two = Shot(self.position.x, self.position.y, self.mods)

            shot_one.velocity = vector_one * 2
            shot_two.velocity = vector_two * 2
        
        if not undestrucible:
            self.kill()


            

