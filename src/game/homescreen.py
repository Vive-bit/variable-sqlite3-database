import pygame


def startIMG(surface):
    startimgraw = pygame.image.load("pictures/Start.png")  # load an image
    startimg = pygame.Surface.convert_alpha(startimgraw)  # optimize blitting
    sizestart = pygame.transform.scale(startimg, (500, 100))
    surface.blit(sizestart, (1920/2-250, 200))

    return sizestart

def settingIMG(surface):
    settingimgraw = pygame.image.load("pictures/Einstellungen.png")  # load an image
    settingimg = pygame.Surface.convert_alpha(settingimgraw)  # optimize blitting
    sizesetting = pygame.transform.scale(settingimg, (500, 100))
    surface.blit(sizesetting, (1920 / 2 - 250, 400))





def update(surface):
    startIMG(surface)


