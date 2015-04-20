from weapon import Weapon
from spell import Spell


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        self.name = name
        self.title = title
        self.health = health
        self.max_health = health
        self.mana = mana
        self.max_mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.mana_cost = 0
        self.damage_by_weapon = 0
        self.damage_by_spell = 0

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        if self.damage_by_spell == 0 or self.mana_cost > self.mana:
            return False
        else:
            return True

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if self.is_alive() is False:
            return False
        heal = self.health + healing_points
        if heal > self.max_health:
            return False
        else:
            self.health = heal
            return True

    def take_mana(self, mana_points):
        pass

    def equip(self, weapon):
        if self.damage_by_weapon > 0:
            raise AttributeError("Hero is already equipped with weapon.")
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

