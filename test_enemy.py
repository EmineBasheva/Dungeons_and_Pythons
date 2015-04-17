from enemy import Enemy
from weapon import Weapon
import unittest


class TestEnemy(unittest.TestCase):
    
    def setUp(self):
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_take_demage(self):
        self.enemy.take_damage(30)
        self.assertEqual(self.enemy._health, 70)

    def test_take_demage_negative(self):
        self.enemy.take_damage(111)
        self.assertEqual(self.enemy._health, 0)

    def test_attack_without_st(self):
        self.assertEqual(self.enemy.attack(), self.enemy._damage)

    def test_attack_with_bla(self):
        self.assertEqual(self.enemy.attack("bla"), self.enemy._damage)

    def test_attack_with_20(self):
        w = Weapon('Axe', 20)
        self.enemy.equip(w)
        self.assertEqual(self.enemy.attack("weapon"), 20)

if __name__ == '__main__':
    unittest.main()