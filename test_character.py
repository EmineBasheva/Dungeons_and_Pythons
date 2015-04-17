from character import Character
from weapon import Weapon
from spell import Spell
import unittest


class TestCharacter(unittest.TestCase):
    
    def setUp(self):
        self.char = Character(health=100, mana=100)

    def test_health_with_negative(self):
        with self.assertRaises(ValueError):
            char2 = Character(health=-100, mana=100)

    def test_mana_negative(self):
        with self.assertRaises(ValueError):
            char2 = Character(health=100, mana=-100)
    
    def test_is_alive_with_100(self):
        self.assertTrue(self.char.is_alive())

    def test_is_alive_with_0_5(self):
        char2 = Character(health=0.5, mana=100)
        self.assertTrue(char2.is_alive())

    def test_can_cast_True(self):
        self.assertTrue(self.char.can_cast())

    def test_can_cast_False(self):
        char2 = Character(health=100, mana=0)
        self.assertFalse(char2.can_cast())

    def test_get_health_100(self):
        self.assertEqual(self.char.get_health(), 100)

    def test_get_mana_100(self):
        self.assertEqual(self.char.get_mana(), 100)

    def test_take_healing_with_True(self):
        char2 = Character(health=100, mana=100)
        char2._health = 20
        self.assertTrue(char2.take_healing(20))

    def test_take_healing_increase_health(self):
        char2 = Character(health=100, mana=100)
        char2._health = 20
        char2.take_healing(20)
        self.assertEqual(char2._health, 40)

    def test_take_healing_False(self):
        char2 = Character(health=100, mana=100)
        char2._health = 0
        char2.take_healing(20)
        self.assertFalse(char2.take_healing(20))

    def test_equip_with_weapon(self):
        w = Weapon('Axe', 20)
        char2 = Character(health=100, mana=100)
        char2.equip(w)
        self.assertEqual(char2.damage_by_weapon, 20)

    def test_equip_with_raise(self):
        with self.assertRaises(AttributeError):
            w = Weapon('Axe', 20)
            char2 = Character(health=100, mana=100)
            char2.equip(w)
            char2.equip(w)

    def test_attack_by_weapon(self):
        w = Weapon('Axe', 20)
        char2 = Character(health=100, mana=100)
        char2.equip(w)
        self.assertEqual(char2.attack("weapon"), 20)

    def test_attack_by_spell(self):
        s = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
        char2 = Character(health=100, mana=100)
        char2.learn(s)
        self.assertEqual(char2.attack("spell"), 30)

    def test_attack_with_not_exist_weapon_spell(self):
        self.assertEqual(self.char.attack(''), 0)


if __name__ == '__main__':
    unittest.main()