import pygame
import random
from asteroid import Asteroid
from constants import *
from powerup.powerup import PowerUp
from powerup.powerupenum import PowerUpEnum

class AsteroidField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]
        
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.asteroid_spawn_timer = 0.0
        self.powerup_spawn_timer = 0.0
        self.powerup_spawn_interval = self.get_powerup_spawn_interval()
        self.spawn_as_now = True

    def draw(self,screen):
        field_border = pygame.Rect(BORDER_POSITIVE_X_OFFSET, BORDER_POSITIVE_Y_OFFSET, SCREEN_WIDTH - BORDER_NEGATIVE_X_OFFSET, SCREEN_HEIGHT - BORDER_NEGATIVE_Y_OFFSET)
        pygame.draw.rect(screen, "WHITE", field_border, 5)

    def update(self, dt):
        self.asteroid_spawn_timer += dt
        self.powerup_spawn_timer += dt

        self.check_asteroid_spawn_timer()
        self.check_powerup_spawn_timer()
    
    def check_asteroid_spawn_timer(self):
        if self.asteroid_spawn_timer > ASTEROID_SPAWN_RATE or self.spawn_as_now:
            self.spawn_as_now = False
            self.asteroid_spawn_timer = 0
            self.spawn_asteroid()

    def check_powerup_spawn_timer(self):
        if self.powerup_spawn_timer > self.powerup_spawn_interval:
            self.powerup_spawn_timer = 0
            self.powerup_spawn_interval = self.get_powerup_spawn_interval()
            self.spawn_powerup()

    def spawn_asteroid(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)

        asteroid = Asteroid(position.x, position.y ,ASTEROID_MIN_RADIUS * kind)
        asteroid.velocity = velocity

    def spawn_powerup(self):
        PowerUp(random.randint(5, SCREEN_WIDTH - 30),
                random.randint(5, SCREEN_HEIGHT - 30),
                random.randint(1, len(PowerUpEnum)),
                random.randint(POWER_UP_MIN_DURATION_INTERVAL, POWER_UP_MAX_DURATION_INTERVAL))
   
    def get_powerup_spawn_interval(self):
        return random.randint(POWER_UP_MIN_SPAWN_INTERVAL, POWER_UP_MAX_SPAWN_INTERVAL)

