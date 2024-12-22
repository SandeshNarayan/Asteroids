# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame 
from asteroid import *
from asteroidfield import *


from constants import *
from player import Player
def main():
    from shot import Shot

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)


    print( "Starting asteroids!" )
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game variables
    '''score = 0
    time_limit = 60  # 1 minute
    start_time = pygame.time.get_ticks()  # Track the start time'''


    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = ( updatable, drawable)
    Asteroid.containers = ( updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield=AsteroidField()

    running = True
    while running:

        dt = clock.tick(60) /1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updatable.update(dt)

        

        # Collision checks
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print('Game over!')  
                running = False   
            
            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        
        ''' # Display score and timer
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
        remaining_time = max(0, time_limit - elapsed_time)
        score_text = font.render(f"Score: {score}", True, "white")
        timer_text = font.render(f"Time: {int(remaining_time)}", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(timer_text, (10, 50))'''

        pygame.display.flip()
        

        '''# End game after time limit
        if remaining_time <= 0:
            print(f"Game Over! Your final score is: {score}")
            running = False'''
        
        asteroidfield.update(dt)
    
    pygame.quit()

if __name__ == "__main__":
    main()