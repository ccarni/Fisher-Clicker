from upgrade import Upgrade
from fish import Fish
import random
from types import MethodType
all_upgrades = []
purchased_upgrades = []
available_upgrades = []
locked_upgrades = []

fish = Fish()

def unlock_generator(min_coins=0, min_cps=0, min_fish_base_value=0, min_fish_mult_value=0, needed_upgrades=[]):
    def unlock(self, coins, cps):
        global purchased_upgrades
        con_coins = coins >= min_coins
        con_cps = cps >= min_cps
        con_base = fish.base_value >= min_fish_base_value
        con_mult = fish.mult_value >= min_fish_mult_value
        con_needed = True
        pur_tags = []
        for pur_upgrade in purchased_upgrades:
            pur_tags.append(pur_upgrade.tag)
        for tag in needed_upgrades:
            if tag not in pur_tags:
                con_needed = False
        if con_coins and con_cps and con_base and con_mult and con_needed:
            return True
        return False

    return unlock

seed = 0
rand = random.Random(seed)

def random_color():
    return [rand.randint(0, 255) for i in range(3)]

all_upgrades.append(Upgrade('Add one to fish base value.',
                            unlock_generator(min_coins=1),
                            1,
                            random_color(),
                            tag='bad'))
all_upgrades[-1].on_click = lambda: fish.update_value(base=1)
all_upgrades.append(Upgrade('Add one to fish mult value.',
                            unlock_generator(needed_upgrades=['bad']),
                            10,
                            random_color(),
                            tag='better'))
all_upgrades[-1].on_click = lambda: fish.update_value(mult=2)
all_upgrades.append(Upgrade('Auto Fisher.',
                            unlock_generator(),
                            75,
                            random_color(),
                            tag='auto'))
all_upgrades[-1].on_click = lambda: fish.update_auto(speed=0.001)
all_upgrades.append(Upgrade('Add one to fish mult value.',
                            unlock_generator(needed_upgrades=['auto']),
                            50,
                            random_color(),
                            tag='meh'))
all_upgrades[-1].on_click = lambda: fish.update_value(mult=3)
all_upgrades.append(Upgrade('Add one to fish base value.',
                            unlock_generator(min_coins=15),
                            25,
                            random_color(),
                            tag='ok'))
all_upgrades[-1].on_click = lambda: fish.update_value(base=3)
all_upgrades.append(Upgrade('Add one to fish base value.',
                            unlock_generator(min_coins=30),
                            30,
                            random_color(),
                            tag='ok2'))
all_upgrades[-1].on_click = lambda: fish.update_value(base=4)

locked_upgrades = all_upgrades[:]
