import pygame
from constants import *
from circleshape import CircleShape
from logger import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        
        log_event("asteroid_split")
        old_rad = self.radius
        new_angle = random.uniform(20, 50)
        
        new_velocity1 = self.velocity.rotate(new_angle)
        new_velocity2 = self.velocity.rotate(-new_angle)

        new_radius = old_rad - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = new_velocity1 * 1.2
        a2.velocity = new_velocity2 * 1.2