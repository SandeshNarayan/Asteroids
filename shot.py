from circleshape import CircleShape
from constants import *
import pygame
from player import *

class Shot(CircleShape):
    def __init__(self, x, y,velocity, angle):
        self.radius = SHOT_RADIUS
        super().__init__(x, y, self.radius)
        self.velocity = velocity

    def draw(self,screen):
        return pygame.draw.circle(screen, "white",(int(self.position.x), int(self.position.y)), self.radius,2)
    
    def update(self, dt):
        self.get_position()[0] += self.get_velocity()[0] * dt
        self.get_position()[1] += self.get_velocity()[1] * dt
