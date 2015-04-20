from character import Character


class Enemy(Character):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        if damage < 0:
            raise ValueError
        self._damage = damage

    def take_damage(self, damage):
        self._health = max(0, self._health - damage)

    def attack(self, by=''):
        if by == 'weapon':
            return self.damage_by_weapon
        elif by == 'spell':
            return self.damage_by_spell
        return self._damage
