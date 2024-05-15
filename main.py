import pygame
import src.game.homescreen as homescreen
import src.game.settingscreen as settingscreen
import src.game.screenupdater.screenloader as sl
global mouse, statusStart, statusSetting, statusQuit, statusSave, statusAudio

pygame.init()

window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
surface = window

pygame.display.set_caption("Halle7")

# Define Var's
statusHomescreen = 1
statusSettingscreen = 0
statusQuit = 0
statusSetting = 0
statusSave = 1
statusAudio = 0

font = pygame.font.Font("fonts/Antreas.ttf", 30)


running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        elif homescreen.startIMG(surface).collidepoint(mouse) and statusQuit == 0:
            pass

        elif homescreen.beendenSureYes(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            running = False

        elif homescreen.beendenSureNo(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusQuit = 0 # Disable "BeendenSure" Window

        elif homescreen.einstellungIMG(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN and statusQuit == 0:
            statusSetting = 1 # Enables "Settingsscreen" Window

        elif homescreen.beendenIMG(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusQuit = 1 # Enable "BeendenSure" Window



        elif settingscreen.settingSaveButton(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            pass

        elif settingscreen.settingCancleButton(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusSetting = 0
            statusSave = 1
            statusAudio = 0

        elif settingscreen.settingSaveBarTopButton(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusSave = 1
            statusAudio = 0

        elif settingscreen.settingAudioBarTopButton(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusSave = 0
            statusAudio = 1




    # Standard window background with 60 FPS setting
    clock = pygame.time.Clock()         # FPS setting = 60FPS
    delta_time = clock.tick(60) / 1000  # FPS setting = 60 FPS
    window.fill((255, 255, 255))        # Filling background to white

    # Update


    # Checks if "Einstellungen" Button is pressed
    if statusSetting == 0 and statusQuit == 0:
        homescreen.updateN(surface)
    elif statusSetting == 0 and statusQuit == 1:
        homescreen.updateQ(surface)
    elif statusSetting == 1 and statusSave == 1:
        settingscreen.updateSaveScreen(surface)
    elif statusSetting == 1 and statusAudio == 1:
        settingscreen.updateAudioScreen(surface)






    pygame.display.update()

pygame.quit()
