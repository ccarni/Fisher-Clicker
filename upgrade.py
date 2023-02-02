import pygame
import gameobject
from types import MethodType

class Upgrade(gameobject.GameObject):
    def __init__(self, text, unlock_condition, cost, color, tag='', size=20):
        gameobject.GameObject.__init__(self)
        self.size = size
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.hover_text = text
        self.unlock = MethodType(unlock_condition, self)

        self.tag = tag
        self.cost = cost

        self.unlocked = False

    def on_click(self):
        print('broken')
        pass