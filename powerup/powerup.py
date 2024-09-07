from circleshape import CircleShape
from powerup.powerupenum import PowerUpEnum
from powerup.powerupconfig import power_up_dict
from constants import *

import pygame

class PowerUp(CircleShape):
    def __init__(self, x, y, radius, type, duration):
        super().__init__(x, y, radius)
        self.type = type
        self.duration = duration
        self.config = power_up_dict[PowerUpEnum(type)]
        self.font = pygame.font.SysFont("arial", POWER_UP_FONT_SIZE)
        self.text = self.font.render(self.config["text"],True, self.config["color"], None)

    def draw(self, screen):
        pygame.draw.circle(screen, self.config["color"], self.position, POWER_UP_RADIUS, 2)
        screen.blit(self.text, self.text.get_rect(center = self.position))


