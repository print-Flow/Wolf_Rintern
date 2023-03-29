import pygame


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.orientation = 0
        self.sprite_sheet = pygame.image.load(f"../assets/{sprite_name}.png")
        self.current_image = 0
        self.cote = 0
        self.direct = direction[self.cote]
        self.images = animations.get(sprite_name, self.direct)
        self.animation = False
        self.nbr_img_par_actions = 4

    # methode de démarage de l'animation
    def start_animation(self, n):
        # n accueil l'orientation
        self.orientation = n
        self.animation = True

    # methode d'animation
    def animate(self):

        if self.animation:
            # passer à l'image suivante
            self.current_image += 1
            if self.current_image >= self.nbr_img_par_actions - 1:
                # recommencer
                self.current_image = 0
                self.animation = False

            self.image = self.images[self.orientation][self.current_image]


direction = ['down', 'left', 'right', 'up']
cote = 0


# charger les images
def load_animation_images(sprite_name, direct):
    global cote
    images = []
    path = f"../assets/{sprite_name}_{direct}/{sprite_name}"

    for num in range(1, 4):
        sprite_sheet_path = path + str(num) + ".png"
        images.append(pygame.image.load(sprite_sheet_path))

    # pour les directions on adapte "images"
    # frame = [images]
    cote += 1

    return images


# dict qui contient les img
animations = {
    'player': (load_animation_images('player', direction[0]), load_animation_images('player', direction[1]),
               load_animation_images('player', direction[2]), load_animation_images('player', direction[3]))
}
