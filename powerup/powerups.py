
import pygame
import random

from spawningobjects import SpawningObjects
from powerup.powerup import PowerUp
from constants import *
from powerup.powerupenum import PowerUpEnum

class PowerUps(SpawningObjects):
    def __init__(self):
        super().__init__()
        self.next_spawn_interval = POWER_UP_MIN_SPAWN_INTERVAL

    def spawn(self, x, y, power_up_type, duration):
        PowerUp(x, y, power_up_type, duration)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.next_spawn_interval:
            self.spawn_timer = 0
            self.next_spawn_interval = random.randint(POWER_UP_MIN_SPAWN_INTERVAL, POWER_UP_MAX_SPAWN_INTERVAL)

            self.spawn(random.randint(5, SCREEN_WIDTH - 30), 
                       random.randint(5, SCREEN_HEIGHT - 30), 
                       random.randint(1, len(PowerUpEnum)), 
                       random.randint(POWER_UP_MIN_DURATION_INTERVAL, POWER_UP_MAX_DURATION_INTERVAL))
        
        


