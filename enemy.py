from character import Character


class Enemy(Character):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self._damage = damage

    def take_damage(self, damage_points):
        self._health = max(self._health - damage_points, 0)

    def attack(self, by=''):
        if by == "weapon":
            return self.damage_by_weapon
        elif by == "spell":
            return self.damage_by_spell
        return self._damage
