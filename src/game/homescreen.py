import pygame
pygame.font.init()

font = pygame.font.SysFont("Arial", 46)
text = font.render("Start", True, "Red")
textRect = text.get_rect()
textRect.center = (1920 / 2, 0)

def draw(surface):
    pygame.draw.rect(surface, "gray", (660, 100, 600, 500))
    pygame.draw.rect(surface, "black", (910, 200, 100, 50))
    surface.blit(text, (960, 200))



def update(surface):
    draw(surface)


