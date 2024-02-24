import pygame, random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Shooting Game')

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

FPS = 60

clock = pygame.time.Clock()
quit = False

tankImg = pygame.image.load('C:/Users/amritmesh/Downloads/final_space_ship_for_game.png')
meteorImg = pygame.image.load('C:/Users/amritmesh/Downloads/final_meteor_for_game.png')
explodeImg1 = pygame.image.load('C:/Users/amritmesh/Downloads/final_explosion_for_game.png')
backgroundImg = pygame.image.load('C:/Users/amritmesh/Downloads/final_background_for_game.png')
#crash_sound = pygame.mixer.Sound("C:/DATASTICK-Copy/Python Class Resources/QLCPython/expl3.wav")
#explodeImg2 = pygame.image.load('C:/DATASTICK-Copy/Python Class Resources/QLCPython/regularExplosion01.png')


#tank_x =  (display_width * 0.45)
#tank_y = (display_height * 0.8)
tank_x = 400
tank_y = 500

x_change = 0
car_speed = 0

meteor_x = random.randint(0,display_width)
meteor_y = 0

shoot = False
bullet_x = 0
bullet_y = 0

gotIt = False

crash_count = 0

def meteor(tank_x,tank_y):
    gameDisplay.blit(meteorImg, (tank_x,tank_y))

def tank(tank_x,tank_y):
    gameDisplay.blit(tankImg, (tank_x,tank_y))


def explode(tank_x,tank_y):
    global crash_count
    gameDisplay.blit(explodeImg1, (tank_x,tank_y))
    crash_count = crash_count + 1    
    pygame.mixer.Sound.play(crash_sound)   
    
    
def hit():             
    global meteor_x,meteor_y
    gameDisplay.blit(explodeImg1, (meteor_x,meteor_y))
    meteor_x = random.randint(0,display_width)
    meteor_y = 0


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display():
    message = "Crash Count: {}".format(crash_count)    
    largeText = pygame.font.Font('freesansbold.ttf',10)
    TextSurf, TextRect = text_objects(message, largeText)
    TextRect.center = (50,10)
    gameDisplay.blit(TextSurf, TextRect)    
#######

while not quit:
    if meteor_y > display_height:
        meteor_y = 0
        meteor_x = random.randint(0,display_width)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif (event.key == pygame.K_SPACE):
                bullet_x = tank_x
                bullet_y = tank_y
                shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################
    ##
    tank_x += x_change
    meteor_y += 5
   ##

    #car_rect = tankImg.get_rect()
    meteor_rect = meteorImg.get_rect()
    meteor_width = meteor_rect.width
    meteor_height = meteor_rect.height
    car_rect = tankImg.get_rect()
    car_width = car_rect.width
    car_height = car_rect.height
    
    #meteor_cur_rect = pygame.Rect(meteor_x,meteor_y,meteor_x+meteor_width,meteor_y+meteor_height)
    #car_cur_rect = pygame.Rect(tank_x,tank_y,tank_x+car_width,tank_y+car_height)
                
    gameDisplay.blit(backgroundImg,(0,0))
    
    if (shoot):
        pygame.draw.rect(gameDisplay, RED, [bullet_x, bullet_y, 5, 10])
        bullet_y += -10
        
    
    if (bullet_x > meteor_x and bullet_x < meteor_x + meteor_width or \
        bullet_x+5 > meteor_x and bullet_x + 5 < meteor_x+meteor_width) and \
        bullet_y > meteor_y and bullet_y < meteor_y + meteor_height:
        print("Hit")        
        hit()
    
    if (tank_x > meteor_x and tank_x < meteor_x + meteor_width or \
        tank_x+car_width > meteor_x and tank_x + car_width < meteor_x+meteor_width) and \
        tank_y < meteor_y + meteor_height:        
        #print("CRASH")        
        explode(tank_x,tank_y)
    else:
        tank(tank_x,tank_y)
        meteor(meteor_x,meteor_y)            

    message_display()                
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
