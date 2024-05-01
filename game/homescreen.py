import pygame
import main

def draw():
    pygame.draw.rect(main.surface, "gray", ([0, 0], [1920, 1080]), 2)


def update():
    draw()


