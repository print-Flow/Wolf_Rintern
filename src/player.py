import pygame
from src import animation


class Player(animation.AnimateSprite):

    def __init__(self, x, y):
        super().__init__("player")
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        # self.orientation = 0 remplacé par slef.orientation = n dans animation.py
#        self.direction = {
#            'down': self.get_image(0, 0),
#            'left': self.get_image(0, 32),
#            'right': self.get_image(0, 64),
#            'up': self.get_image(0, 96)
#        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 4)
        self.old_position = self.position.copy()
        self.speed = 3

    def save_location(self): self.old_position = self.position.copy()

#    def change_direction(self, name):
#        self.image = self.direction[name]
#        self.image.set_colorkey((0, 0, 0))

    def move_right(self):
        self.position[0] += self.speed
        self.start_animation(2)

    def move_left(self):
        self.position[0] -= self.speed
        self.start_animation(1)

    # plus d'info pour permettre le multidirectionel, les diagonales /\
    def move_up(self):
        self.position[1] -= self.speed
        self.start_animation(3)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move_right()
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move_left()

    def move_down(self):
        self.position[1] += self.speed
        self.start_animation(0)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.move_right()
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.move_left()
    # plus d'info pour permettre le multidirectionel, les diagonales /\

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def update_animation(self):
        self.animate()

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
