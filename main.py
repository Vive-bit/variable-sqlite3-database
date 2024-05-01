import pygame

pygame.init()

window_width = 1920
window_height = 1080
window = pygame.display.set_mode((window_width, window_height))
surface = window

running = True
while running:
    import game.homescreen
    game.homescreen.update()
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        elif event.type == pygame.KEYDOWN and pygame.key == pygame.K_ESCAPE:
            running = False
    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()