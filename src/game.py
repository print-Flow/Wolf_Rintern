import pygame
from player import Player
from src.map import MapManager


class Game:

    def __init__(self):
        self.walls = list[pygame.Rect]

        # fenêtre
        self.screen = pygame.display.set_mode((1680, 989))
        pygame.display.set_caption("Rintern - Aventure")

        # generer un joueur
        self.player = Player(0, 0)
        self.map_manager = MapManager(self.screen, self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            # self.player.change_direction('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            # self.player.change_direction('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            # self.player.change_direction('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            # self.player.change_direction('right')

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.player.update_animation()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()
