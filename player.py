from circleshape import CircleShape
from constants import *
from shot import Shot
from powerup.powerupenum import PowerUpEnum

import pygame

class Player(CircleShape):
    def __init__(self,x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.powerups = {}

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt) 
        
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.update_powerups(dt)    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position + forward * PLAYER_SPEED * dt
        print(position.y)
        if not self.check_border_collision(position):
            self.position += forward * PLAYER_SPEED * dt    

    def shoot(self):
        if not self.timer > 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            if PowerUpEnum.FAST_SHOT.value in self.powerups:
                self.timer /= 3

            new_shot = Shot(self.position.x, self.position.y, self.powerups)
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

            if PowerUpEnum.TRIPLE_SHOT.value in self.powerups:
                new_shot = Shot(self.position.x, self.position.y, self.powerups)
                new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation - 20) * PLAYER_SHOOT_SPEED

                new_shot = Shot(self.position.x, self.position.y, self.powerups)
                new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation + 20) * PLAYER_SHOOT_SPEED
    
    def check_border_collision(self,position):
        return ((position.x - self.radius <= BORDER_RIGHT_OFFSET or 
                position.x + self.radius >= SCREEN_WIDTH - BORDER_LEFT_OFFSET) or
                (position.y - self.radius <= BORDER_TOP_OFFSET or
                position.y + self.radius >= SCREEN_HEIGHT - BORDER_BOTTOM_OFFSET))

    def get_powerup(self, new_powerup):
        self.powerups[new_powerup.type] = new_powerup    
        new_powerup.kill()
        return        

    def update_powerups(self,dt):
        if self.powerups:
            for powerup in self.powerups:
                self.powerups[powerup].effect_duration -= dt

            self.powerups = {k:v for (k,v) in self.powerups.items() if v.effect_duration > 0}

