import pygame


def settingoverlay(surface):
    pygame.draw.rect(surface, "gray", [(1560, 850), (100, 50)]) # Draw "Save" Button
    pygame.draw.rect(surface, "gray", [(1410, 850), (100, 50)]) # Draw "Cancel" Button

def settingSaveBarTop(surface):
    pygame.draw.rect(surface, "darkgray", [(210, 100), (750, 40)])  # Settings Save Files

def settingAudioBarTop(surface):
    pygame.draw.rect(surface, "darkgray", [(960, 100), (750, 40)])  # Setting Audio

def settingSaveScreen(surface):
    pygame.draw.rect(surface, "lightgray", [(210, 140), (1500, 800)])  # Draw settings background 1

def settingAudioScreen(surface):
    pass

def updateSaveScreen(surface):
    settingSaveScreen(surface)
    settingoverlay(surface)

def updateAudioScreen(surface):
    settingAudioScreen(surface)
    settingoverlay(surface)

