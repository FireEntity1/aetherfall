#!/usr/bin/env python2

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

pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aetherfall")
clock = pygame.time.Clock()

xPos, yPos = 20, 350
gravity = 0.6
jumpHeight = 10
yVelocity = jumpHeight
jumping = False
speed = 6
screenPos = 0

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
        if yVelocity < -jumpHeight and yPos > 350:
            jumping = False
            yVelocity = jumpHeight
    if keys_pressed[pygame.K_d]:
        xPos += speed
        playerSprite = noFlipSprite
    if keys_pressed[pygame.K_a]:
        xPos -= speed
        playerSprite = pygame.transform.flip(noFlipSprite, 1, 0)

    # sidescrolling
    if xPos > 350:
        screenPos -= speed
        xPos -= speed
    if xPos < 50:
        screenPos += speed
        xPos += speed

    # draw sprites 'n stuff!!
    screen.blit(bg, (screenPos,0)) # background
    screen.blit(playerSprite, (xPos,yPos)) # player

    pygame.display.flip()       

pygame.quit()