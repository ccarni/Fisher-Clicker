import pygame
import sys
import fish
import upgrade
import upgradelist
import random
import pond_draw

def draw_pond(surf, rect, pond_surf):
    surf.blit(pond_surf, (surf.get_rect().x, surf.get_rect().y))
    pygame.draw.rect(surf, (255, 255, 255), surf.get_rect(), width=1)

def draw_upgrades(surf, rect, upgrades):
    surf.fill((0, 0, 0))
    pygame.draw.rect(surf, (255, 255, 255), surf.get_rect(), width=1)
    x = 0
    y = 0
    width = upgradelist.all_upgrades[0].rect.width
    i_count_value = width + 5
    for upgrade in upgrades:
        upgrade.rect.x = rect.x + x
        upgrade.rect.y = rect.y + y
        surf.blit(upgrade.image, [x, y])

        x += i_count_value
        if x > surf.get_width() - width:
            x = 0
            y += i_count_value


def draw_hover(surf, rect, hover, font):
    surf.fill((0, 0, 0))
    pygame.draw.rect(surf, (255, 255, 255), surf.get_rect(), width=1)
    if hover:
        text = font.render(hover.hover_text, True, (255, 255, 255))
        surf.blit(text, (10, 10))
        if isinstance(hover, upgrade.Upgrade):
            text = font.render(f'Cost: {hover.cost}', True, (255, 255, 255))
            surf.blit(text, (10, 30))


class Runner:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font(None, 30)
        self.surf = pygame.display.set_mode(flags=pygame.FULLSCREEN )

        self.cps = 0.01
        self.coins = 0
        self.fps = 30
        self.clock = pygame.time.Clock()

        self.pond_colors = [(10, 10, 255), (135, 156, 19), (95, 110, 12), (112, 61, 19), (163, 75, 3), (3, 40, 163),
                            (6, 105, 148), (11, 89, 122), (81, 142, 168)]

        self.pond_image = pond_draw.screener(self.surf, random.choice(self.pond_colors))

        self.screen_y = self.surf.get_height() / 2
        self.title_padding = 50

        self.pond_surf = pygame.Surface((600,900 - self.title_padding))
        self.pond_rect = self.pond_surf.get_rect()
        self.pond_rect.x = 0
        self.pond_rect.y += self.title_padding
        # self.pond_rect.y = self.screen_y - (self.pond_rect.height / 2)
        self.upgrade_surf = pygame.Surface((400, 900 - self.title_padding))
        self.upgrade_rect = self.upgrade_surf.get_rect()
        self.upgrade_rect.x = self.pond_rect.x + self.pond_rect.width
        self.upgrade_rect.y += self.title_padding
        # self.upgrade_rect.y = self.screen_y - (self.upgrade_rect.height / 2)
        self.hover_surf = pygame.Surface((600, 900 - self.title_padding))
        self.hover_rect = self.hover_surf.get_rect()
        self.hover_rect.x = self.surf.get_width() - self.hover_rect.width
        self.hover_rect.y += self.title_padding
        # self.hover_rect.y = self.screen_y - (self.hover_rect.height / 2)

        self.hoverables = pygame.sprite.Group()
        self.fish = fish.Fish(bounds=self.pond_rect)
        self.fish.bounds = self.pond_rect


        self.auto_timer = 0
        self.max_auto_time = self.fish.auto

        self.current_hover = None

    def update_pond_image(self):
        self.pond_image = pond_draw.screener(self.surf, random.choice(self.pond_colors))

    def update(self):
        self.cps = self.fish.auto
        dt = self.clock.tick(self.fps)
        self.coins += dt*self.cps

        for upgrade in upgradelist.locked_upgrades:
            if upgrade.unlock(self.coins, self.cps):
                upgradelist.locked_upgrades.remove(upgrade)
                upgradelist.available_upgrades.append(upgrade)



    def draw(self):
        self.surf.fill((0, 0, 0))


        draw_pond(self.pond_surf, self.pond_rect, self.pond_image)
        draw_hover(self.hover_surf, self.hover_rect, self.current_hover, self.font)
        draw_upgrades(self.upgrade_surf, self.upgrade_rect, upgradelist.available_upgrades)

        self.surf.blit(self.pond_surf, self.pond_rect)
        self.surf.blit(self.hover_surf, self.hover_rect)
        self.surf.blit(self.upgrade_surf, self.upgrade_rect)

        self.surf.blit(self.fish.image, self.fish.rect)

        #Write coins text
        coins_padding = 10
        coin_text = self.font.render(f'Coins: {round(self.coins)}', True, (255, 255, 0))
        self.surf.blit(coin_text, (self.hover_rect.x + coins_padding,
                              self.hover_rect.y + self.hover_rect.height - coin_text.get_height() - coins_padding))

        # base
        text = self.font.render(f'Base: {round(self.fish.base_value)}', True, (255, 255, 255))
        self.surf.blit(text, (self.hover_rect.centerx - (text.get_width() / 2),
                              self.hover_rect.y + self.hover_rect.height - text.get_height() - coins_padding))

        # Multiplier
        multiplier_text = self.font.render(f'Multiplier: {round(self.fish.mult_value)}', True, (255, 255, 255))
        self.surf.blit(multiplier_text, (self.hover_rect.x + coins_padding + 450,
                              self.hover_rect.y + self.hover_rect.height - multiplier_text.get_height() - coins_padding))


        #Write upgrades title
        padding = (0, 30)
        text = self.font.render('Upgrades', True, (0, 255, 0))
        x = self.upgrade_rect.centerx - (text.get_width() / 2)
        self.surf.blit(text, (x + padding[0],
                              self.upgrade_rect.y - padding[1]))

        #pond title
        text = self.font.render('Pond', True, (100, 100, 255))
        x = self.pond_rect.centerx - (text.get_width() / 2)
        self.surf.blit(text, (x + padding[0],
                              self.upgrade_rect.y - padding[1]))

        #hover title
        text = self.font.render('Info', True, (255, 255, 255))
        x = self.hover_rect.centerx - (text.get_width() / 2)
        self.surf.blit(text, (x + padding[0],
                              self.upgrade_rect.y - padding[1]))
        pygame.display.update()

    def get_input(self):
        mouse_pos = pygame.mouse.get_pos()
        self.current_hover = ''
        for upgr in upgradelist.available_upgrades:
            if upgr.rect.collidepoint(mouse_pos):
                self.current_hover = upgr

        if self.fish.rect.collidepoint(mouse_pos):
            self.current_hover = self.fish

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.current_hover:
                        if self.current_hover == self.fish:
                            self.coins += self.current_hover.on_click()
                            self.update_pond_image()
                        if isinstance(self.current_hover, upgrade.Upgrade):
                            if self.coins >= self.current_hover.cost:
                                self.current_hover.on_click()
                                upgradelist.available_upgrades.remove(self.current_hover)
                                upgradelist.purchased_upgrades.append(self.current_hover)
                                self.coins -= self.current_hover.cost
