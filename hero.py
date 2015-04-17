from character import Character
from weapon import Weapon


class Hero(Character):

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        super().__init__(health, mana)
        self.name = name
        self.title = title
        self.mana_regeneration_rate = mana_regeneration_rate
        self.damage_by_weapon = 0

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def take_damage(self, damage_points):
        self._health = max(self._health - damage_points, 0)

