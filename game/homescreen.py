import pygame
import main

def draw():
    pygame.draw.rect(main.surface, "gray", (50, 50, 400, 600), 10)      #
    return True

def update():
    draw()
    #import main
    #main.screen="none"

