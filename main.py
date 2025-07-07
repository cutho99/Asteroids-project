import pygame, constants

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #Set screen size
    
    clock = pygame.time.Clock()                             #Create a clock object to track time
    dt = 0

    while True:
        for event in pygame.event.get():                    #Check if user close the window
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")                #Fill screen w solid black
        pygame.display.flip()                               #Refreshes the screen to update colour
        clock.tick(60)                                      #Pauses the game loop for 1/60 second
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

