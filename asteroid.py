from circleshape import CircleShape
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       # self.velocity = self.get_velocity()
        

    def draw(self,screen):
        return pygame.draw.circle(screen, "white",(int(self.position.x), int(self.position.y)), self.radius,2)
    
    def update(self, dt):
        self.get_position()[0] += self.get_velocity()[0] * dt
        self.get_position()[1] += self.get_velocity()[1] * dt