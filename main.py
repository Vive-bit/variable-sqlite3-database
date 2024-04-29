import pygame
from dice import Dices


class Start:
    def __init__(self):
        pygame.init()
        # Window setup
        self.window_width = 1920
        self.window_height = 1080
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.surface = self.window

        # Title
        pygame.display.set_caption("Kniffel")

        # Define the class from a file / run()
        self.dices = Dices(self)
        self.run()

    def run(self):
        running = True
        # mouse = pygame.mouse.get_pos()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pass
            # Default setting
            self.clock = pygame.time.Clock()
            self.delta_time = self.clock.tick(60) / 1000  # FPS setting = 60 FPS
            self.window.fill((0, 0, 0))  # Background (Before updating [drawing] on surface)

            # Update
            # print(mouse)
            self.dices.update()

            pygame.display.update()
    pygame.quit()


game = Start()
