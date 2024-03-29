# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:00:42 2021

@author: user
"""

import pygame
from pygame import rect
from pygame.locals import *
import time

BLACK = (0,0,0)
RED = (255,0,0)
GRAY = (200,200,200)

pygame.init()
screen = pygame.display.set_mode((640,240))
pygame.display.set_caption('Smooth Movement')

text = "RIDHO WALIDHAYIN RIFAI"
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (20,20)
cursor = Rect(rect.topright, (3, rect.height))

running = True
baground = GRAY

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]

            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size = img.get_size()
            cursor.topleft = rect.topright

    screen.fill(baground)
    screen.blit(img,rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

pygame.quit()