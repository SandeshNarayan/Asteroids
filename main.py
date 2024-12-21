# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame 

#import everything from constants.py

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print( "Starting asteroids!" )
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #Use an infinite while loop for the game loop. At each iteration, it should:
    #Use the screen's fill method to fill the screen with a solid "black" color.
    #Use pygame's display.flip() method to refresh the screen. Be sure to call this last!
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()