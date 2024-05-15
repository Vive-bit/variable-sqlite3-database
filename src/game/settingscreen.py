import pygame
lightgray = "lightgray"
gray = "gray"
darkgray = "darkgray"
red = "red"
blue = "blue"


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
    pygame.draw.rect(surface, red, [(210, 100), (750, 40)], 2)  # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Speicherstand", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (210 + (750 - textwidth) / 2, 100 + (40 - textheight) / 2))

    return x
def settingAudioBarTopButton(surface):
    x = pygame.draw.rect(surface, darkgray, [(960, 100), (750, 40)]) # Draw "Save" Button
    pygame.draw.rect(surface, red, [(960, 100), (750, 40)], 2)  # Draw "Save" Button
    font = pygame.font.Font("fonts/Antreas.ttf", 30)
    text = font.render("Audio", True, red)
    textwidth = text.get_rect().width
    textheight = text.get_rect().height

    surface.blit(text, (960 + (750 - textwidth) / 2, 100 + (40 - textheight) / 2))

    return x
def settingVolume(surface):
    pygame.draw.line(surface, blue, (300, 300), (700, 300), 6)
    d1 = pygame.draw.circle(surface, red, (300, 300), 10)  # 0%
    d2 = pygame.draw.circle(surface, red, (400, 300), 10)  # 25%
    d3 = pygame.draw.circle(surface, red, (500, 300), 10)  # 50%
    d4 = pygame.draw.circle(surface, red, (600, 300), 10)  # 75%
    d5 = pygame.draw.circle(surface, red, (700, 300), 10)  # 100%

    return d1, d2, d3, d4, d5
def settingSaveScreen(surface):
    pygame.draw.rect(surface, lightgray, [(210, 140), (1500, 800)])  # Draw settings background 1


def settingAudioScreen(surface):
    pygame.draw.rect(surface, lightgray, [(210, 140), (1500, 800)])  # Draw settings background 1
    settingVolume(surface)

def updateSaveScreen(surface):
    settingSaveBarTopButton(surface)
    settingAudioBarTopButton(surface)
    settingSaveScreen(surface)
    settingCancleButton(surface)
    settingSaveButton(surface)

def updateAudioScreen(surface):
    settingAudioBarTopButton(surface)
    settingSaveBarTopButton(surface)
    settingAudioScreen(surface)
    settingCancleButton(surface)
    settingSaveButton(surface)

