from circleshape import CircleShape
import pygame
import random

from player import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       # self.velocity = self.get_velocity()
        

    def draw(self,screen):
        return pygame.draw.circle(screen, "white",(int(self.position.x), int(self.position.y)), self.radius,2)
    
    def update(self, dt):
        self.get_position()[0] += self.get_velocity()[0] * dt
        self.get_position()[1] += self.get_velocity()[1] * dt

    def check_collision(self, shot):
        if self.position.distance_to(shot.position) < self.radius +shot.radius:
            return True
        return False
    
    def split(self):
        self.kill( )
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle=random.uniform(20,50)
        vector1=self.velocity.rotate(angle)
        vector2=self.velocity.rotate(-angle)
        new_radius = self.radius- ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.set_velocity(vector1*1.2)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.set_velocity(vector2*1.2)

    def set_velocity(self, velocity):
        self.velocity = velocity