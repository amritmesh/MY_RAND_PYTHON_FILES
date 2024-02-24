import pygame

WIDTH = 500
HEIGHT = 300

RED  = (255,0,0)
BLUE = (0,0,255)
NEON_GREEN = (0,255,0)
LIME_GREEN = (50,205,50)
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHT_PINK = (255,182,193)
LIGHT_BLUE = (173,216,230)
CYAN = (0,255,255)
SADDLE_BROWN = (139,69,19)
DARK_GREEN = (0,100,0)
SNOW_4 = (139,137,137)
GOLD = (255,215,0)
LIGHT_CYAN = (224,255,255)

pygame.init()

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Initialization")

clock = pygame.time.Clock()
FPS = 20

display_surface.fill(CYAN)

def grass():
    pygame.draw.line(display_surface, LIME_GREEN, (0,300), (500,300), 100)

def left_tree():
    pygame.draw.rect(display_surface, SADDLE_BROWN, (40,182,30,70), 0)
    pygame.draw.circle(display_surface, DARK_GREEN, (55,175), 35, 0)

def right_tree():
    pygame.draw.rect(display_surface, SADDLE_BROWN, (429,182,30,70), 0)
    pygame.draw.circle(display_surface, DARK_GREEN, (444,175), 35, 0)

def house():
    pygame.draw.rect(display_surface, RED, (168,96,160,156), 0)
    pygame.draw.polygon(display_surface, SNOW_4, ((168,96), (250,40), (327,96)))
    pygame.draw.rect(display_surface, SADDLE_BROWN, (228,192,40,60), 0)
    pygame.draw.circle(display_surface, GOLD, (260,222), 3, 0)

    pygame.draw.rect(display_surface, LIGHT_CYAN, (185,138,36,36), 0)
    pygame.draw.line(display_surface, BLACK, (185,138), (220,138), 5)
    pygame.draw.line(display_surface, BLACK, (185,173), (220,173), 5)
    pygame.draw.line(display_surface, BLACK, (185,138), (185,173), 5)
    pygame.draw.line(display_surface, BLACK, (220,138), (220,173), 5)
    pygame.draw.line(display_surface, BLACK, (202,138), (202,173), 5)
    pygame.draw.line(display_surface, BLACK, (185,156), (220,156), 5)

    pygame.draw.rect(display_surface, LIGHT_CYAN, (275,138,36,36), 0)
    pygame.draw.line(display_surface, BLACK, (275,138), (310,138), 5)
    pygame.draw.line(display_surface, BLACK, (275,173), (310,173), 5)
    pygame.draw.line(display_surface, BLACK, (275,138), (275,173), 5)
    pygame.draw.line(display_surface, BLACK, (310,138), (310,173), 5)
    pygame.draw.line(display_surface, BLACK, (292,138), (292,173), 5)
    pygame.draw.line(display_surface, BLACK, (275,156), (310,156), 5)

running = True
while running:

    events = pygame.event.get()
    
    for event in events:
        print(pygame.event.event_name(event.type))
        if(event.type == pygame.QUIT):
            running = False

    grass()
    left_tree()
    right_tree()
    house()
        
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
