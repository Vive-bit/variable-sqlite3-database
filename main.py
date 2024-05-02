import pygame
import src.game.homescreen as homescreen
global mouse

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
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("Highnachtsmann")

    # Standard window background with 60FPS setting

    clock = pygame.time.Clock()         # FPS setting = 60FPS
    delta_time = clock.tick(60) / 1000  # FPS setting = 60 FPS
    window.fill((255, 255, 255))        # Filling background to white

    # Update

    homescreen.update(surface)          # Homescreen design updating

    pygame.display.update()

pygame.quit()
