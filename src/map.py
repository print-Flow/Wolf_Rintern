from dataclasses import dataclass
import pygame
import pyscroll
import pytmx
from pytmx import TiledObject

#r = pygame.Rect(0, 1, 2, 3)
#print(r)


@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap


class MapManager:

    def __init__(self, screen, player):
        # correction de tuple object is not callable
        self.maps = dict()  # "house" -> Map("house", walls, group)
        self.tuple = ()
        self.screen = screen
        self.player = player
        self.current_map = "world"

        self.register_map("world")
        self.register_map("house")

        self.teleport_player("player")

    def check_collisions(self):
        for sprite in self.get_group().sprites():
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name):
        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(f"../map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 3

        # definir une liste qui va stoquer les rectanges de collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "border_collision" or "water_collision" or "object_collision":
                self.tuple = pygame.rect.Rect(obj.x, obj.y, obj.width, obj.height)
                walls.append(self.tuple)

        # dessiner le grp de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=8)
        group.add(self.player)

        # créer un obj map
        self.maps[name] = Map(name, walls, group, tmx_data)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()