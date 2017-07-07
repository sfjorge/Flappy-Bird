#Adding gravity

import pygame
import random 

pygame.init()

loss = pygame.mixer.Sound('loss.wav')
flap = pygame.mixer.Sound('flap.wav')
point = pygame.mixer.Sound('point.wav')

black = (0,0,0)
white = (255,255,255)
skyBlue = (0,191,255)
green = (0,255,0)
red = (255,0,0)
orange = (255, 215, 0)
gray = (112,138,144)

size = (400,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()

dead = False
x_bg = 0
y_bg = 0
x1_bg = 400
x = 200
y = 250
x_speed = 0
y_speed = 0
ground = 447
xloc=400
yloc = 0
xsize = 70
ysize = random.randint(5,230)
space = 150
obspeed = 2.5
score = 0
acc = 0.4 
highScore = 0

def obstacles(xloc,yloc,xsize,ysize):
    imgTop = pygame.image.load('pipe.png')
    imgBottom = pygame.image.load('pipe.png')
    imgTop = pygame.transform.rotate(imgTop, 180)
    imgTop = pygame.transform.scale(imgTop, (xsize, ysize))
    imgBottom = pygame.transform.scale(imgBottom, (xsize, 500 - ysize))
    
    screen.blit(imgTop, (xloc, yloc))
    screen.blit(imgBottom, (xloc, int(yloc + ysize + space)))

imageUp = pygame.image.load('flappy_up.png')
imageDown = pygame.image.load('flappy_down.png')
imageUp = pygame.transform.scale(imageUp, (40,40))
imageDown = pygame.transform.scale(imageDown, (80,40))
imageDead = pygame.image.load('deadBlue.png')
imageDead = pygame.transform.scale(imageDead, (28,23))

def move_background(x_bg, x1_bg, y_bg):
    background = pygame.image.load('background.png')
    background = pygame.transform.scale(background, (400,500))  
    screen.blit(background, (x_bg,y_bg))
    screen.blit(background, (x1_bg, y_bg))
    
def move_ground(x_bg, x1_bg, y_bg):
    ground = pygame.image.load('ground.png')
    ground = pygame.transform.scale(ground, (400,60))    
    screen.blit(ground,(x_bg,470))
    screen.blit(ground, (x1_bg,470))
    
def flappy(x,y, y_speed, alive):
    if alive == True:
        if y_speed < 0:
            #falling image
            screen.blit(imageUp, (x,y))
        elif y_speed >= 0:
            #flapping image
            screen.blit(imageDown, (x-20,y-10))
    elif alive == False:
        screen.blit(imageDead, (x + 10,y))
            
def gameover():
    font = pygame.font.SysFont(None,50)
    text = font.render("Game Over ",True,red)
    screen.blit(text, [200,250])

#function to write score being kept
def Score(score):
    font = pygame.font.SysFont(None,70)
    text = font.render(str(score),True,white)
    screen.blit(text, [200,62])
    
def high_score(highScore):
    font = pygame.font.SysFont(None,30)
    text = font.render("High Score: "+str(highScore),True,black)
    screen.blit(text, [250,0])
    
    
def splash_screen():
    splash = True
    while splash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                splash = False
        screen.fill(white)
        font = pygame.font.SysFont(None,60)
        text = font.render("SANTOS Code",True,black)
        screen.blit(text, [50,200])
        font2 = pygame.font.SysFont(None, 20)
        text2 = font2.render("(Press any key to continue...)", True, gray)
        screen.blit(text2, [50,300])
        pygame.display.update()
        clock.tick(40)
            
def game_intro():
    intro = True
    play = False
    quit = False
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
            if quit == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    pygame.quit()
            if play == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    intro = False
                
        screen.fill(skyBlue)
        
        mouse = pygame.mouse.get_pos()
        
        move_background(x_bg, x1_bg, y_bg)
        move_ground(x_bg, x1_bg, y_bg)
        flappy(x,y,y_speed, not dead) 
        
        if 50 + 100 > mouse[0] > 50 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(screen, red, (50,400,100,50))
            pygame.draw.rect(screen, green, (250,400,100,50))
            play = True
        elif 250 + 100 > mouse[0] > 250 and 400 + 50 > mouse[1] > 400:
            pygame.draw.rect(screen, red, (250,400,100,50))
            pygame.draw.rect(screen, green, (50,400,100,50))
            quit = True
        else:
            play = False
            quit = False
            pygame.draw.rect(screen, green, (50,400,100,50))
            pygame.draw.rect(screen, green, (250,400,100,50))
        font = pygame.font.SysFont(None,55)
        text1 = font.render("PLAY",True,white)
        text2 = font.render("QUIT",True,white)
        screen.blit(text1, [50,400])
        screen.blit(text2, [250,400])
        font2 = pygame.font.SysFont(None, 60)
        text3 = font2.render("FLAPPY BIRD!", True, orange)
        screen.blit(text3, [50,50])
        
        pygame.display.update()
        clock.tick(40)
        
def game_loop():   
    done = False
    alive = True
    x_bg = 0
    y_bg = 0
    x1_bg = 400
    x = 200
    y = 250
    y_speed = 0
    ground = 447
    xloc=400
    yloc = 0
    xsize = 70
    ysize = random.randint(5,230)
    space = 150
    obspeed = 2.5
    score = 0

    highScore = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_speed = -7
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alive = True
                    x_bg = 0
                    y_bg = 0
                    x1_bg = 400
                    x = 200
                    y = 250
                    y_speed = 0
                    ground = 447
                    xloc=400
                    yloc = 0
                    xsize = 70
                    ysize = random.randint(0,350)
                    space = 150
                    obspeed = 2.5
                    score = 0
                    game_intro()

        screen.fill(skyBlue) 

        move_background(x_bg, x1_bg, y_bg)
        if alive == True:
            x_bg -= obspeed * (2.0/3)
            x1_bg -= obspeed * (2.0/3)
            #width divided by to = 200
            if x_bg + 400 < 0:
                x_bg = 400 
            if x1_bg + 400 < 0:
                x1_bg = 400

            obstacles(xloc,yloc,xsize,ysize)
            move_ground(x_bg, x1_bg, y_bg)
            flappy(x,y,y_speed, alive)    
            #if the ball is between to obstacles 
            Score(score)
            high_score(highScore)

            y_speed += acc
            y += y_speed
            xloc -= obspeed
            if score >= highScore:
                highScore = score
            elif score < highScore:
                highScore
            if y > ground:
                gameover()
                y_speed = 0 
                obspeed = 0
                alive = False

            #if we hit obstacles in the top block
            if x+40 > xloc and y < ysize and x-15 < xsize+xloc:
                gameover()
                obspeed = 0
                y_speed = 0
                alive = False

            #if we hit obstacles in the bottom block
            if x+30 > xloc and y+25 > ysize+space and x-15 < xsize+xloc:
                gameover()
                obspeed = 0
                y_speed = 0
                alive = False

            #if obstacle location X is 
            if xloc < -80:
                xloc = 400
                ysize = random.randint(0,350)

            #check if obstacle was passed adding to score
            if x > xloc and x < xloc+3:
                score = (score + 1)
                point.play()
        elif alive == False:
            obstacles(xloc,yloc,xsize,ysize)
            move_ground(x_bg, x1_bg, y_bg)
            flappy(x,y,y_speed, alive)    
            #if the ball is between to obstacles 
            Score(score)
            high_score(highScore)
            gameover()
            if y <= ground:
                y += 6

        pygame.display.flip()
        clock.tick(40)

    pygame.quit()
    
splash_screen()
pygame.mixer.music.load('bgMusic.wav')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.1)
game_intro()
game_loop()
print "High Score: " + str(highScore)
