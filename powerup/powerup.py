from shape import Shape
from powerup.powerupenum import PowerUpEnum
from powerup.powerupconfig import power_up_dict
from constants import *

import pygame

class PowerUp(Shape):
    def __init__(self, x, y, power_up_type, duration):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.type = power_up_type
        self.duration = duration
        self.time_spawned = 0
        self.config = power_up_dict[PowerUpEnum(power_up_type)]
        self.font = pygame.font.SysFont("arial", POWER_UP_FONT_SIZE)
        self.text = self.font.render(self.config["text"],True, self.config["color"], None)
        self.effect_duration = 30

    def draw(self, screen):
        pygame.draw.circle(screen, self.config["color"], self.position, POWER_UP_RADIUS, 2)
        screen.blit(self.text, self.text.get_rect(center = self.position))

    def update(self, dt):
        self.time_spawned += dt
        if self.time_spawned > self.duration:
            self.kill()


