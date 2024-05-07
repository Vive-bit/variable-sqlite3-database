import pygame
import src.game.homescreen as homescreen
global mouse, statusStart, statusSetting, statusQuit

pygame.init()

window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
surface = window

pygame.display.set_caption("Halle7")

# Define Var's
statusQuit = 0

running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

        elif homescreen.beendenSureYes(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            running = False

        elif homescreen.beendenSureNo(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusQuit = 0 # Disable "BeendenSure" Window

        elif homescreen.startIMG(surface).collidepoint(mouse):
            pass

        elif homescreen.einstellungIMG(surface).collidepoint(mouse):
            pass

        elif homescreen.beendenIMG(surface).collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            statusQuit = 1 # Enable "BeendenSure" Window





    # Standard window background with 60 FPS setting
    clock = pygame.time.Clock()         # FPS setting = 60FPS
    delta_time = clock.tick(60) / 1000  # FPS setting = 60 FPS
    window.fill((255, 255, 255))        # Filling background to white

    # Update

    # Checks if "BeendenSure" Window should appear
    if statusQuit == 0:
        homescreen.updateN(surface)     # Homescreen design updating when "No"
    else:
        homescreen.updateQ(surface)     # Homescreen design updating when "Yes"

    pygame.display.update()

pygame.quit()
