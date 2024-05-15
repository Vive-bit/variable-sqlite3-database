import pygame
lightgray = "lightgray"
gray = "gray"
darkgray = "darkgray"
red = "red"


def settingSaveButton(surface):
    x = pygame.draw.rect(surface, gray, [(1560, 850), (100, 50)]) # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Speichern", True, "red")
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (1560 + (100 - textwidth) / 2, 850 + (50 - textheight) / 2))

    return x
def settingCancleButton(surface):
    x = pygame.draw.rect(surface, gray, [(1410, 850), (100, 50)]) # Draw "Cancel" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Abbrechen", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (1410 + (100 - textwidth) / 2, 850 + (50 - textheight) / 2))

    return x
def settingCancleRect(surface):
    pass

def settingCancleButtonYes(surface):
    pass

def settingCancleButtonNo(surface):
    pass




def settingSaveBarTopButton(surface):
    x = pygame.draw.rect(surface, darkgray, [(210, 100), (750, 40)]) # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Speicherstand", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (1560 + (100 - textwidth) / 2, 850 + (50 - textheight) / 2))

    return x
def settingAudioBarTopButton(surface):
    x = pygame.draw.rect(surface, darkgray, [(960, 100), (750, 40)]) # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Audio", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (1560 + (100 - textwidth) / 2, 850 + (50 - textheight) / 2))

    return x
def settingSaveScreen(surface):
    x = pygame.draw.rect(surface, lightgray, [(210, 140), (1500, 800)])  # Draw settings background 1

    return x
def settingAudioScreen(surface):
    pass

def updateSaveScreen(surface):
    settingSaveBarTopButton(surface)
    settingSaveScreen(surface)
    settingCancleButton(surface)
    settingSaveButton(surface)

def updateAudioScreen(surface):
    settingAudioBarTopButton(surface)
    settingAudioScreen(surface)
    settingCancleButton(surface)
    settingSaveButton(surface)

