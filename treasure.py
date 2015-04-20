from weapon import Weapon
from spell import Spell
import random


class Treasure:
    
    treasures = ["healing", "mana potion", "weapon", "spell"]
    spells = [Spell("Fireball", 30, 20, 2), Spell("Iceball", 20, 10, 2),
              Spell("Bomb", 35, 35, 2), Spell("Bla", 5, 5, 1)]
    weapons = [Weapon("Axe", 30), Weapon("Knife", 5), Weapon("Sword", 15)]

    def get_treasure(self, hero):
        random_treasure = random.choice(treasures)
        if random_treasure == "healing":
            hero.take_healing(random.randint(10, 25))

        elif random_treasure == "mana potion":
            hero.take_mana(random.randint(10, 25))

        elif random_treasure == "weapon":
            hero.equip(random.choice(weapons))
            
        elif random_treasure == "spell":
            hero.learn(random.choice(spells))

    def __init__(self, hero):
        self.get_treasure(hero)

