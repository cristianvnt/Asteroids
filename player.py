import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cd = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "purple", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_a]):
            self.rotate(-dt)

        if (keys[pygame.K_d]):
            self.rotate(dt)

        if (keys[pygame.K_w]):
            self.move(dt)

        if (keys[pygame.K_s]):
            self.move(-dt)

        if (keys[pygame.K_SPACE]):
            self.shoot()
            self.shoot_cd -= dt

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        vec = pygame.Vector2(0, 1)
        rotated = vec.rotate(self.rotation)
        rotated_speed = rotated * PLAYER_SPEED * dt
        self.position += rotated_speed

    def shoot(self):
        if self.shoot_cd > 0:
            return
        self.shoot_cd = PLAYER_SHOTS_COOLDOWN_SECONDS

        vec = pygame.Vector2(0, 1)
        direction = vec.rotate(self.rotation)
        direction = direction.normalize()
        offset = self.radius * 1.5
        spawn_pos = self.position + direction * offset

        shot = Shot(spawn_pos.x, spawn_pos.y, SHOT_RADIUS)
        shot.velocity = direction * PLAYER_SHOOT_SPEED