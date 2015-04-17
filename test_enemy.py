from enemy import Enemy
from weapon import Weapon
import unittest


class TestEnemy(unittest.TestCase):
    
    def setUp(self):
        self.enemy = Enemy(health=100, mana=100, damage=20)

    def test_damage_negative(self):
        with self.assertRaises(ValueError):
            enemy2 = Enemy(health=100, mana=100, damage=-20)

    def test_take_damage(self):
        enemy2 = Enemy(health=100, mana=100, damage=20)
        enemy2.take_damage(30)
        self.assertEqual(enemy2._health, 70)

    def test_attack_with_weapon(self):
        w = Weapon('Axe', 30)
        self.enemy.equip(w)
        self.assertEqual(self.enemy.attack('weapon'), 30)

    def test_attack(self):
        self.assertEqual(self.enemy.attack(), 20)

if __name__ == '__main__':
    unittest.main()