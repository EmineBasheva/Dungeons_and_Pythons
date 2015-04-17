from weapon import Weapon
from spell import Spell


class Character:

    def __init__(self, health, mana):
        if health < 0:
            raise ValueError
        self.__max_health = health
        self._health = health
        if mana < 0:
            raise ValueError
        self.__max_mana = mana
        self._mana = mana
        self.damage_by_weapon = 0
        self.mana_cost = 0
        self.damage_by_spell = 0

    def is_alive(self):
        return self._health > 0

    def can_cast(self):
        if not self.is_alive():
            return False
        return self._mana > 0

    def get_health(self):
        return self._health

    def get_mana(self):
        return self._mana

    def take_mana(self, mana_points):
        pass

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        self._health = min(self.__max_health, self._health + healing_points)
        return True

    def equip(self, weapon):
        if self.damage_by_weapon > 0:
            raise AttributeError("Already equipped with weapon.")
        else:
            self.damage_by_weapon = weapon.get_damage()

    def learn(self, spell):
        self.damage_by_spell = spell.get_damage()
        self.mana_cost = spell.get_mana_cost()

    def attack(self, by):
        if self.damage_by_weapon == 0 and self.damage_by_spell == 0:
            return 0
        if by is "weapon":
            return self.damage_by_weapon
        if by is "spell":
            return self.damage_by_spell

