from shape import Shape
from constants import *
from screendimensions.screendimensions import *
from screendimensions.screencoordinatesenum import *

import pygame
import random

class Asteroid(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.already_split = False
        self.border_collision = False

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self,dt):
        self.position += (self.velocity * dt)

        ## Check if inside the game board
        if ((self.position.x - self.radius > BORDER_RIGHT_OFFSET and self.position.x + self.radius < SCREEN_WIDTH - BORDER_LEFT_OFFSET) and
            (self.position.y - self.radius > BORDER_TOP_OFFSET and self.position.y + self.radius < SCREEN_HEIGHT - BORDER_BOTTOM_OFFSET)):
                self.border_collision = True

    def check_border_collision(self):
         if self.border_collision:
            if (self.position.x - self.radius <= screencoordinates[ScreenCoordinatesEnum.LEFT] or 
                self.position.x + self.radius >= screencoordinates[ScreenCoordinatesEnum.RIGHT]):
                self.velocity[0] *= -1
            if (self.position.y - self.radius <= screencoordinates[ScreenCoordinatesEnum.TOP] or
                self.position.y + self.radius >= screencoordinates[ScreenCoordinatesEnum.BOTTOM]):
                self.velocity[1] *= -1            
                   
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS or self.already_split:
            return
        
        self.already_split = True
        random_angle = random.uniform(20, 50)
        
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)

        asteroid_one = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_two = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

        asteroid_one.velocity = vector_one * 1.2
        asteroid_two.velocity = vector_two * 1.2
