import pygame
import src.game.homescreen as homescreen
global mouse, statusStart, statusSetting

pygame.init()

window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
surface = window

pygame.display.set_caption("Halle7")

running = True
while running:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif homescreen.startIMG(surface).collidepoint(mouse):
            print("Start")
        elif homescreen.einstellungIMG(surface).collidepoint(mouse):
            print("Einstellung")
        elif homescreen.beendenIMG(surface).collidepoint(mouse) and event.type == pygame.KEYDOWN and\
                event.key == pygame.MOUSEBUTTONDOWN:
            homescreen.beendensure(surface)

        elif homescreen.beendenIMG(surface).collidepoint(mouse):
            print("Beenden")
        elif event.type == pygame.KEYDOWN and event.key == pygame.MOUSEBUTTONDOWN:
            print("allah")

    # Standard window background with 60FPS setting

    clock = pygame.time.Clock()         # FPS setting = 60FPS
    delta_time = clock.tick(60) / 1000  # FPS setting = 60 FPS
    window.fill((255, 255, 255))        # Filling background to white

    # Update

    homescreen.update(surface)          # Homescreen design updating

    pygame.display.update()

pygame.quit()
