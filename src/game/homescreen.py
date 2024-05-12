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
    #pygame.draw.rect(surface, "yellow", [(1920/2-250, 1080/2-200), (500, 400)])   # Draw the quit box
    beendensureboximgraw = pygame.image.load("pictures/BeendenSureBox.png") # Load an image
    beendensureboximg = pygame.Surface.convert_alpha(beendensureboximgraw) # Optimize image
    sizebeendensurebox = pygame.transform.scale(beendensureboximg, (500, 400)) # Set size of image
    x = surface.blit(sizebeendensurebox, (1920 / 2 - 250, 1080 / 2 - 200))

    pygame.draw.rect(surface, "red", [(1920 / 2 - 250, 1080 / 2 - 200), (500, 400)], 4)  # Draw the quit box outline
    pygame.draw.rect(surface, "black", [(1920 / 2 - 230, 1080 / 2 + 75), (160, 100)])  # Draw the quit box buttons box 1
    pygame.draw.rect(surface, "red", [(1920 / 2 - 230, 1080 / 2 + 75), (160, 100)], 4)  # Draw the quit box buttons box outlines 1
    pygame.draw.rect(surface, "black", [(1920 / 2 + 70, 1080 / 2 + 75), (160, 100)])  # Draw the quit box buttons box 2
    pygame.draw.rect(surface, "red", [(1920 / 2 + 70, 1080 / 2 + 75), (160, 100)], 4)  # Draw the quit box buttons box outlines 2

    return x


def beendenSureYes(surface): # Quit sure button
    beendensureyesimgraw = pygame.image.load("pictures/BeendenText.png")  # Load an image
    beendensureyesimg = pygame.Surface.convert_alpha(beendensureyesimgraw)  # Optimize image
    sizebeendensureyes = pygame.transform.scale(beendensureyesimg, (100, 50))  # Set size of image
    x = surface.blit(sizebeendensureyes, (1920 / 2 - 200, 1080 / 2 + 100))

    return x

def beendenSureNo(surface): # Quit not button
    beendensurenoimgraw = pygame.image.load("pictures/AbbrechenText.png")  # Load an image
    beendensurenoimg = pygame.Surface.convert_alpha(beendensurenoimgraw)  # Optimize image
    sizebeendensureno = pygame.transform.scale(beendensurenoimg, (100, 50))  # Set size of image
    x = surface.blit(sizebeendensureno, (1920 / 2 + 100, 1080 / 2 + 100))

    return x

def beendenSureText(surface): # Quit sure text
    beendensuretextimgraw = pygame.image.load("pictures/BeendenSureText.png")       # Load an image
    beendensuretextimg = pygame.Surface.convert_alpha(beendensuretextimgraw)        # Optimize image
    sizebeendensuretext = pygame.transform.scale(beendensuretextimg, (500, 250))    # Set size of image
    x = surface.blit(sizebeendensuretext, (1920/2-250, 1080/2-200))

    return x

def updateN(surface): # Update when not "BeendenSure"
    backgroundIMG(surface)
    startIMG(surface)
    einstellungIMG(surface)
    beendenIMG(surface)

def updateQ(surface): # Update when "BeendenSure"
    backgroundIMG(surface)
    beendenSureRect(surface)
    beendenSureYes(surface)
    beendenSureNo(surface)
    beendenSureText(surface)





