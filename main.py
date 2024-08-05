import pygame
import random
import math


WIDTH = 400
HEIGHT = 400
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100,100,100)

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aetherfall")
clock = pygame.time.Clock()

isText = True
loaded = False
floorLevel = 350
level = 1
xPos, yPos = 20, 350

gravity = 0.6
jumpHeight = 10
yVelocity = jumpHeight
jumping = False
speed = 6
screenPos = 0
font = pygame.font.SysFont('Courier', 15)
currentText = font.render(" ", False, BLACK)
falling = False

def move(x,y):
    global xPos
    global yPos
    xPos, yPos = x, y

def limit(min,max):
    global xPos
    global yPos
    if xPos < min:
        xPos = min
    if xPos > max:
        xPos = max

bg = pygame.image.load("mapBg.png")
bg = pygame.transform.scale(bg,(4000,400))

playerSprite = pygame.image.load("player.png")
noFlipSprite = pygame.transform.scale(playerSprite,(32,32))
playerSprite = noFlipSprite

running = True
while running:
    clock.tick(FPS)   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys_pressed = pygame.key.get_pressed()

    # movement
    if keys_pressed[pygame.K_SPACE]:
        jumping = True
    if jumping:
        yPos -= yVelocity
        yVelocity -= gravity
        if yPos > floorLevel:
            jumping = False
            yVelocity = jumpHeight
    if keys_pressed[pygame.K_d]:
        xPos += speed
        playerSprite = noFlipSprite
    if keys_pressed[pygame.K_a]:
        xPos -= speed
        playerSprite = pygame.transform.flip(noFlipSprite, 1, 0)


    # level specific
    if level == 0:
        isText = True
        if xPos > 350:
            screenPos -= speed
            xPos -= speed
        if xPos < 50:
            screenPos += speed
            xPos += speed
        if screenPos > 0:
            screenPos = 0
        if screenPos < -3050:
            level = 1
        if screenPos < -2100:
            currentText = font.render('HELP US. . .', False, WHITE)
        elif screenPos <  -1300:
            currentText = font.render("Our sun died out, and everything with it", False, WHITE)
        elif screenPos < -500:
            currentText = font.render("Then the withering happened", False, WHITE)
        elif screenPos < 500:
            currentText = font.render("This place used to be beautiful", False, WHITE)

    if level == 1:
        if loaded == False:
            isText = False
            screenPos = 0
            while WIDTH < 700:
                WIDTH += 2
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            bg = pygame.image.load("level1.png")
            xPos = 50
            yPos = 330
            floorLevel = 330
            isText = True
            currentText = font.render("I need to re-light the sun", False, WHITE)
            loaded = True
        if (xPos > 140 and xPos < 240) or (xPos > 410 and xPos < 510):
            floorLevel = 600
            if jumping == False:
                yVelocity = 0
                jumping = True
        else:
            if yPos > 200: 
                floorLevel = 330
            elif yPos < 200:
                floorLevel = 150
        if yPos > 364:
            xPos, yPos = 50, 330
        if xPos > 650 and yPos > 200:
            floorLevel = 150
            yPos = 150
        if xPos > 600:
            yVelocity = 0
            yPos = 150
            floorLevel = 130
        if xPos < 10 and yPos < 200:
            level = 2
            loaded = False
        limit(0,700)
    if level == 2:
        if loaded == False:
            isText = True
            while WIDTH < 1000:
                WIDTH += 2
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while HEIGHT > 200:
                HEIGHT -= 2
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            xPos = 50
            yPos = 150
            bg = pygame.image.load("level2.png")
            currentText = font.render("But how...", False, WHITE)
            loaded = True
            floorLevel = 150
        if (120 < xPos < 200) or (330 < xPos < 420) or (590 < xPos < 670) or (770 < xPos < 850):
            if jumping == False:
                yVelocity = 0
                jumping = True
                floorLevel = 600
                if yPos > 150:
                    move(50,150)
        else: floorLevel = 150
        limit(0,1000)
        if xPos > 990:
            level = 3
            loaded = False
    if level == 3:
        if loaded == False:
            isText = True
            while WIDTH > 600:
                WIDTH -= 3
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while HEIGHT < 300:
                HEIGHT += 2
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            loaded = True

    # draw sprites 'n stuff!!
    screen.blit(bg, (screenPos,0)) # background
    screen.blit(playerSprite, (xPos,yPos)) # player
    if isText == True:
        pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
        screen.blit(currentText, (25,25)) # text

    pygame.display.flip()

pygame.quit()