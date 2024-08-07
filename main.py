import pygame
import random
import math
import time


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
level = 5
xPos, yPos = 20, 350

hasStone = False
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

pygame.display.set_icon(noFlipSprite)

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
                WIDTH += 4
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
                WIDTH += 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while HEIGHT > 200:
                HEIGHT -= 4
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
                WIDTH -= 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while HEIGHT < 300:
                HEIGHT += 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            screen = pygame.display.set_mode((600, 300))
            bg = pygame.image.load("level3.png")
            currentText = font.render("Oh! A sign!", False, WHITE)
            move(50,250)
            floorLevel = 250
            loaded = True
        if xPos > 206 and yPos > 245:
            move(50,250)
        elif 260 < xPos < 480 and yPos < 194:
            floorLevel = 194
            if jumping == False:
                yVelocity = 0
                jumping = True
            currentText = font.render("You must relight the sun's core with. . .", False, WHITE)
        elif 530 < xPos and yPos > 150:
            floorLevel = 150
            currentText = font.render("The rest was faded.", False, WHITE)
            if jumping == False:
                yVelocity = 0
                jumping = True
        elif xPos < 206:
            floorLevel = 250
            currentText = font.render("Oh! A sign!", False, WHITE)
        else: floorLevel = 600
        
        if xPos > 600:
            level = 4
            loaded = False
        limit(0, 601)

    if level == 4:
        if loaded == False:
            while WIDTH > 300:
                WIDTH -= 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while HEIGHT > 300:
                HEIGHT -= 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            move(50,250)
            bg = pygame.image.load("level4.png")
            screen.blit(bg, (screenPos,0))
            floorLevel = 250
            loaded = True
            time.sleep(0.2)
            cutsceneIndex = 0
        match cutsceneIndex:
            case 0:
                currentText = font.render("Hello.", False, WHITE)
                time.sleep(3)
                cutsceneIndex += 1
            case 1:
                currentText = font.render("In order to get to the sun...", False, WHITE)
                time.sleep(3)
                cutsceneIndex += 1
            case 2:
                currentText = font.render("You must make your way...", False, WHITE)
                time.sleep(3)
                cutsceneIndex += 1
            case 3:
                currentText = font.render("To the core", False, WHITE)
                time.sleep(3)
                cutsceneIndex += 1
            case 4:
                currentText = font.render("And use the Sunstone", False, WHITE)
                time.sleep(4)
                cutsceneIndex += 1
            case 5:
                currentText = font.render("I believe in you", False, WHITE)
        if xPos > 300:
            level = 5
            loaded = False

    if level == 5:
        floor = 0
        if loaded == False:
            while HEIGHT < 700:
                HEIGHT += 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while WIDTH > 300:
                WIDTH -= 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            currentText = font.render("If I can get up there..", False, WHITE)
            move(50, 658)
            bg = pygame.image.load("level5.png")
            floorLevel = 655
            loaded = True
        if 70 < xPos < 200:
            if yPos > (floorLevel):
                move(5, floorLevel)
        else:
            if yPos < 500:
                floorLevel = 480
    
        if xPos > 260:
            if yPos > 650:
                floorLevel = 480
                move(5,floorLevel)
                currentText = font.render("I'll be able to save this place!", False, WHITE)
            else:
                level = 6
                loaded = False

    if level == 6:
        if loaded == False:
            while HEIGHT > 600:
                HEIGHT -= 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            while WIDTH < 800:
                WIDTH += 4
                screen = pygame.display.set_mode((WIDTH, HEIGHT))
            screen = pygame.display.set_mode((800, 600))
            bg = pygame.image.load("level6.png")
            floorLevel = 525
            move(5,525)
            currentText = font.render("The sunstone! I can feel it!", False, WHITE)
            loaded = True
        if (130 < xPos < 240) or (330 < xPos < 430) or (530 < xPos < 630):
            floorLevel = 800
            if yPos < 350 and jumping == False:
                yVelocity = 0
                jumping = True
            if yPos >= (floorLevel - 30) and jumping == False:
                yVelocity = 0
                jumping = True
            if yPos > 525 - 5:
                move(5,525)
        else:
            if yPos > 300:
                floorLevel = 525
            else:
                floorLevel = 250
        if xPos > 775:
            if yPos > 300:
                floorLevel = 250
                move(5,275)
                currentText = font.render("Just.. a little.. further..", False, WHITE)
            elif yPos < 300:
                level = 7
                loaded = False

        if level == 7:
            if loaded == False:
                while HEIGHT > 600:
                    HEIGHT -= 4
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                while WIDTH < 600:
                    WIDTH += 4
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                screen = pygame.display.set_mode((600, 600))
                bg = pygame.image.load("level7.png")
                move(5,525)
                currentText = font.render("Found it!!", False, WHITE)
                screen.blit(bg, (screenPos,0)) # background
                screen.blit(playerSprite, (xPos,yPos)) # player
                pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
                screen.blit(currentText, (5,25)) # text
                pygame.display.flip()
                time.sleep(4)

                currentText = font.render("Now all I have to do is get this to the sun!", False, WHITE)
                screen.blit(bg, (screenPos,0)) # background
                screen.blit(playerSprite, (xPos,yPos)) # player
                pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
                screen.blit(currentText, (5,25)) # text
                pygame.display.flip()
                move(500,525)
                time.sleep(4)
                level = 8

        if level == 8:
            if loaded == False:
                bg = pygame.image.load("sun1.png")
                floorLevel = 450
                move(5,450)
                screen.blit(bg, (screenPos,0)) # background
                screen.blit(playerSprite, (xPos,yPos)) # player
                pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
                screen.blit(currentText, (5,25)) # text
                pygame.display.flip()
                
                time.sleep(4)
                move(525,450)
                currentText = font.render("So, close...", False, WHITE)
                screen.blit(bg, (screenPos,0)) # background
                screen.blit(playerSprite, (xPos,yPos)) # player
                pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
                screen.blit(currentText, (5,25)) # text
                pygame.display.flip()

                time.sleep(4)
                bg = pygame.image.load("sun2.png")
                move(250,450)
                currentText = font.render("DONE!!", False, WHITE)
                screen.blit(bg, (screenPos,0)) # background
                screen.blit(playerSprite, (xPos,yPos)) # player
                pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
                screen.blit(currentText, (5,25)) # text
                pygame.display.flip()

                time.sleep(4)

                bg=pygame.image.load("black.png")
                currentText = font.render("THE END.", False, WHITE)
                while WIDTH > 2:
                    WIDTH -= 2
                    HEIGHT -= 2
                    screen = pygame.display.set_mode((WIDTH, HEIGHT))
                    if WIDTH < 20:
                        pygame.quit()

    # screen update
    screen.blit(bg, (screenPos,0)) # background
    screen.blit(playerSprite, (xPos,yPos)) # player
    if isText == True:
        if level != 5:
            pygame.draw.rect(screen, GREY, pygame.Rect(0, 0, 1000, 60)) # textbox
            screen.blit(currentText, (5,25)) # text
        elif level == 5:
            pygame.draw.rect(screen, GREY, pygame.Rect(0, 200, 1000, 60)) # textbox lower
            screen.blit(currentText, (5,225)) # text lower
    pygame.display.flip()

pygame.quit()