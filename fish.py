import pygame
import random
import gameobject

# class SubFish:
#     def __init__(self):
#         this does all the original fish stuff

@gameobject.singleton
class Fish(gameobject.GameObject):
    def draw_fish(self):
        screen = pygame.Surface((self.size, self.size))
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.66, screen.get_height() * 0.4,
                                                           screen.get_width() * 0.2, screen.get_height() * 0.2),
                         border_radius=50)

        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.35, screen.get_height() * 0.22,
                                                           screen.get_width() * 0.35, screen.get_height() * 0.06),
                         border_radius=50)
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.35, screen.get_height() * 0.72,
                                                           screen.get_width() * 0.35, screen.get_height() * 0.06),
                         border_radius=50)
        pygame.draw.rect(screen, (90, 70, 68), pygame.Rect(screen.get_width() * 0.25, screen.get_height() * 0.25,
                                                           screen.get_width() * 0.5, screen.get_height() * 0.5),
                         border_radius=50)
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.8, screen.get_height() * 0.3,
                                                           screen.get_width() * 0.08, screen.get_height() * 0.4),
                         border_radius=20)
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.4, screen.get_height() * 0.4,
                                                           screen.get_width() * 0.15, screen.get_height() * 0.1),
                         border_radius=20)
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.82, screen.get_height() * 0.3,
                                                           screen.get_width() * 0.12, screen.get_height() * 0.07),
                         border_radius=20)
        pygame.draw.rect(screen, (70, 50, 48), pygame.Rect(screen.get_width() * 0.82, screen.get_height() * 0.63,
                                                           screen.get_width() * 0.12, screen.get_height() * 0.07),
                         border_radius=20)
        pygame.draw.rect(screen, (1, 1, 1), pygame.Rect(screen.get_width() * 0.3, screen.get_height() * 0.4,
                                                        screen.get_width() * 0.05, screen.get_height() * 0.05),
                         border_radius=100)
        pygame.draw.rect(screen, (250, 250, 250), pygame.Rect(screen.get_width() * 0.33, screen.get_height() * 0.41,
                                                              screen.get_width() * 0.01, screen.get_height() * 0.01),
                         border_radius=100)
        pygame.draw.rect(screen, (50, 50, 50),
                         pygame.Rect(screen.get_width() * 0.25, screen.get_height() * 0.55, screen.get_width() * 0.05,
                                     screen.get_height() * 0.02), border_radius=5)
        screen.set_colorkey((0,0,0))
        return screen

    def __init__(self, size=60, bounds = pygame.Rect(0,0,600,900)):
        gameobject.GameObject.__init__(self)
        self.bounds = bounds
        self.base_value = 1
        self.mult_value = 1
        self.size = size
        self.image = self.draw_fish()
        self.rect = self.image.get_rect()
        self.new_loc()

        self.base = 1
        self.mult = 1
        self.auto = 0

        # This handles the fish_list
        fish_list = []

        self.hover_text = f'A fish worth {self.base_value*self.mult_value} coins'

    def update_value(self, base=0, mult=1):
        self.base_value += base
        self.mult_value *= mult
        # self.base = base_value
        # self.mult = mult_value

        self.hover_text = f'A fish worth {round(self.base_value * self.mult_value, 2)} coins'

    def update_auto(self, speed=0):
        print('done')
        self.auto = speed
        self.update_value(self.base, self.mult)

    def new_loc(self):
        self.rect.x = random.randint(self.bounds.x, self.bounds.x + self.bounds.width - self.image.get_width())
        self.rect.y = random.randint(self.bounds.y, self.bounds.y + self.bounds.height - self.image.get_height())
    def on_click(self):
        self.new_loc()
        return self.base_value * self.mult_value
