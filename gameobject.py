import pygame

# This can be used as a decorator (see fish.py) to make all instances of a class the same
def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton

class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((0, 0))
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.hover_text = ''
