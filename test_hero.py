from hero import Hero
import unittest


class TestHero(unittest.TestCase):
    
    def setUp(self):
        self.h = Hero(name="Bron", title="DragonSlayer",
                      health=100, mana=100, mana_regeneration_rate=2)

    def test_known_as(self):
        self.assertEqual(self.h.known_as(), 'Bron the DragonSlayer')

    def test_take_damage(self):
        self.h.take_damage(20)
        self.assertEqual(80, self.h.get_health())


if __name__ == '__main__':
    unittest.main()
