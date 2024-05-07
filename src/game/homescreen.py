import pygame

def backgroundIMG(surface):
    backgroundimgraw = pygame.image.load("pictures/PalfingerHintergrund.png")
    backgroundimg = pygame.Surface.convert_alpha(backgroundimgraw)
    sizebackground = pygame.transform.scale(backgroundimg, (1920, 1080))
    x = surface.blit(sizebackground, (0, 0))

    return x
def startIMG(surface):
    startimgraw = pygame.image.load("pictures/Start.png")       # Load an image
    startimg = pygame.Surface.convert_alpha(startimgraw)        # Optimize image
    sizestart = pygame.transform.scale(startimg, (500, 100))    # Set size of image
    x = surface.blit(sizestart, (1920/2-250, 200))

    return x

def einstellungIMG(surface):
    settingimgraw = pygame.image.load("pictures/Einstellungen.png")     # Load an image
    settingimg = pygame.Surface.convert_alpha(settingimgraw)            # Optimize image
    sizesetting = pygame.transform.scale(settingimg, (500, 100))        # Set size of image
    x = surface.blit(sizesetting, (1920 / 2 - 250, 300))

    return x


def beendenIMG(surface):
    beendenimgraw = pygame.image.load("pictures/Beenden.png")  # Load an image
    beendenimg = pygame.Surface.convert_alpha(beendenimgraw)  # Optimize image
    sizebeenden = pygame.transform.scale(beendenimg, (500, 100))  # Set size of image
    x = surface.blit(sizebeenden, (1920 / 2 - 250, 400))

    return x
def beendensure(surface):
    pygame.draw.rect(surface, "gray", [(1920/2-250, 1080/2-200), (500, 400)])



def update(surface):
    backgroundIMG(surface)
    startIMG(surface)
    einstellungIMG(surface)
    beendenIMG(surface)
    #beendensure(surface)



