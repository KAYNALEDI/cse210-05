import pygame
import time
import random

pygame.init()

display_width=1280
display_height=720

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
beige=(165,42,42)

bicycle_width=60


gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Cycle")
clock=pygame.time.Clock()

BicycleA=pygame.image.load("bicycle1.png")
BicycleB=pygame.image.load("bicycle2.png")

def bicycle1(x,y):
    gameDisplay.blit(BicycleA,(x,y))

def bicycle2(x,y):
    gameDisplay.blit(BicycleB,(x,y))

def things(thingx,thingy,thingw,thingh,color):
    color=beige

    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
    textSurface=font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect=text_objects(text, largeText)
    TextRect.center=((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    game_loop()

def message_display2(text):
    largeText=pygame.font.Font('freesansbold.ttf',35)
    TextSurf, TextRect=text_objects(text, largeText)
    TextRect.center=((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

def cycle(bicycle):
    message_display('Player'+bicycle+'Cycle')
    

def cycle3():
    message_display('Oops')

def game_loop():
    thing_speed=0
    gameDisplay.fill(white)

    message_display2('Choose a level : Easy-1 Medium-2 Hard-3 BRUTAL-4')
    while(thing_speed==0):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    thing_speed=4
                elif event.key==pygame.K_2:
                    thing_speed=8
                elif event.key==pygame.K_3:
                    thing_speed=16
                elif event.key==pygame.K_4:
                    thing_speed=32

    y_change=0
    y2_change=0

    x=(display_width*0.48/2)
    y=(display_height*0.79)

    x2=(display_width*0.48*1.5)
    y2=(display_height*0.79)

    x_change=0
    x2_change=0

    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_width=50
    thing_height=50

    dodged=0

    gameExit=False

    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x_change=-8
                    y_change=0
                elif event.key==pygame.K_d:
                    x_change=8
                    y_change=0
                elif event.key==pygame.K_w:
                    x_change=0
                    y_change=-8
                elif event.key==pygame.K_s:
                    x_change=-0
                    y_change=8
                if event.key==pygame.K_LEFT:
                    x2_change=-8
                    y2_change=0
                elif event.key==pygame.K_RIGHT:
                    x2_change=8
                    y2_change=0
                elif event.key==pygame.K_UP:
                    x2_change=0
                    y2_change=-8
                elif event.key==pygame.K_DOWN:
                    x2_change=-0
                    y2_change=8

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT or event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    x2_change=0
                    y2_change=0
                if event.key==pygame.K_d or event.key==pygame.K_a or event.key==pygame.K_s or event.key==pygame.K_w:
                    x_change=0
                    y_change=0

        x+=x_change
        if y+y_change>=display_height*0.79:
            y_change=0
        elif y+y_change<=0:
            y_change=0
        y+=y_change

        x2+=x2_change
        if y2+y2_change>=display_height*0.79:
            y2_change=0
        elif y2+y2_change<=0:
            y2_change=0
        y2+=y2_change

        gameDisplay.fill(white)

        things(thing_startx,thing_starty,thing_width,thing_height,black)
        thing_starty+=thing_speed
        bicycle1(x,y)
        bicycle2(x2,y2)

        if ((x+bicycle_width>x2 and x<x2+bicycle_width) and (y-125<y2 and y>y2-125)):
            # print('Collide')
            cycle3()

        if x>display_width-bicycle_width or x<0:
            cycle('1')
        if x2>display_width-bicycle_width or x2<0:
            cycle('2')

        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            if thing_speed<20:
                thing_speed+=0.3

        if y<thing_starty+thing_height:
            # print('y crossover')

            if ((x>thing_startx and x<thing_startx+thing_width) and (y>thing_starty and y<thing_starty+thing_height)) or ((x+bicycle_width>thing_startx and x+bicycle_width<thing_startx+thing_width) and (y>thing_starty and y<thing_starty+thing_height)):
                # print('x crossover')
                cycle('1')
        if y2<thing_starty+thing_height:
            # print('y2 crossover')

            if ((x2>thing_startx and x2<thing_startx+thing_width) and (y2>thing_starty and y2<thing_starty+thing_height)) or ((x2+bicycle_width>thing_startx and x2+bicycle_width<thing_startx+thing_width) and (y2>thing_starty and y2<thing_starty+thing_height)):
                # print('x crossover')
                cycle('2')

        pygame.display.update()
        clock.tick(60)
        
game_loop()
pygame.quit()
quit()

