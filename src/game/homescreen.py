
import pygame
def backgroundIMG(surface): # Background
    backgroundimgraw = pygame.image.load("pictures/PalfingerHintergrund.png")
    backgroundimg = pygame.Surface.convert_alpha(backgroundimgraw)
    sizebackground = pygame.transform.scale(backgroundimg, (1920, 1080))
    x = surface.blit(sizebackground, (0, 0))

    return x

def startIMG(surface): # Start Button
    startimgraw = pygame.image.load("pictures/Start.png")       # Load an image
    startimg = pygame.Surface.convert_alpha(startimgraw)        # Optimize image
    sizestart = pygame.transform.scale(startimg, (500, 100))    # Set size of image
    x = surface.blit(sizestart, (1920/2-250, 200))

    return x

def einstellungIMG(surface): # Settings Button
    settingimgraw = pygame.image.load("pictures/Einstellungen.png")     # Load an image
    settingimg = pygame.Surface.convert_alpha(settingimgraw)            # Optimize image
    sizesetting = pygame.transform.scale(settingimg, (500, 100))        # Set size of image
    x = surface.blit(sizesetting, (1920 / 2 - 250, 300))

    return x

def beendenIMG(surface): # Quit Button
    beendenimgraw = pygame.image.load("pictures/Beenden.png")  # Load an image
    beendenimg = pygame.Surface.convert_alpha(beendenimgraw)  # Optimize image
    sizebeenden = pygame.transform.scale(beendenimg, (500, 100))  # Set size of image
    x = surface.blit(sizebeenden, (1920 / 2 - 250, 400))

    return x
def beendenSureRect(surface):  # "Sure you want to quit" Buttons and Window
    pygame.draw.rect(surface, "gray", [(1920/2-250, 1080/2-200), (500, 400)])   # Draw the quit box

def beendenSureYes(surface):
    beendensureyesimgraw = pygame.image.load("pictures/BeendenText.png")  # Load an image
    beendensureyesimg = pygame.Surface.convert_alpha(beendensureyesimgraw)  # Optimize image
    sizebeendensureyes = pygame.transform.scale(beendensureyesimg, (100, 50))  # Set size of image
    x = surface.blit(sizebeendensureyes, (1920 / 2 - 200, 1080 / 2 + 100))

    return x

def beendenSureNo(surface):
    beendensurenoimgraw = pygame.image.load("pictures/AbbrechenText.png")  # Load an image
    beendensurenoimg = pygame.Surface.convert_alpha(beendensurenoimgraw)  # Optimize image
    sizebeendensureno = pygame.transform.scale(beendensurenoimg, (100, 50))  # Set size of image
    x = surface.blit(sizebeendensureno, (1920 / 2 + 100, 1080 / 2 + 100))

    return x
def updateN(surface):
    backgroundIMG(surface)
    startIMG(surface)
    einstellungIMG(surface)
    beendenIMG(surface)

def updateQ(surface):
    backgroundIMG(surface)
    beendenSureRect(surface)
    beendenSureYes(surface)
    beendenSureNo(surface)





