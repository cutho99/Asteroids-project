import pygame, constants

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  #Set screen size
    
    while True:
        for event in pygame.event.get():                    #Check if user close the window
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")                #Fill screen w solid black
        pygame.display.flip()                               #Refreshes the screen to update colour

if __name__ == "__main__":
    main()

