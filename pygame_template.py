import pygame

WIDTH = 400
HEIGHT = 500

RED  = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_PINK = (255,182,193)
LIGHT_BLUE = (173,216,230)

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Initialization")

clock = pygame.time.Clock()
FPS = 20  

running = True
while running:

    events = pygame.event.get()
    
    for event in events:
        print(pygame.event.event_name(event.type))
        if(event.type == pygame.QUIT):
            running = False

    display_surface.fill(BLUE)
    
    for n in range(0, 400):
        pygame.draw.rect(display_surface, WHITE, (n,100,1,1), 1)
    
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
