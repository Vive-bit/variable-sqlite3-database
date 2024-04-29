import pygame
import time

pygame.init()
# Window setup
window_width = 700
window_height = 700
window = pygame.display.set_mode((window_width, window_height))
surface = window
screen = "homescreen"
# Title
pygame.display.set_caption("Halle7")

def checker():
    if screen == "homescreen":
        import game.homescreen
        x=game.homescreen.draw()
        if x==True:
            game.homescreen.update()
    elif screen == "settingscreen":
        import game.settingscreen
        x = game.homescreen.draw()
        if x == True:
            game.homescreen.update()

def run():
        running = True
        # mouse = pygame.mouse.get_pos()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    #Dices(self).update()



            # Default setting
            clock = pygame.time.Clock()
            delta_time = clock.tick(60) / 1000  # FPS setting = 60 FPS
            window.fill((0, 0, 0))  # Background (Before updating [drawing] on surface)

            # Update
            # print(mouse)
            #dices.update()

            pygame.display.update()
            checker()
    #pygame.quit()
run()
