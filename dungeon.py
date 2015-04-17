"""
lines = open("name of file").read().split("\n")
lines = [line for line in lines if line.strip()!=""]
map = [list(line) for line in lines]


S means a starting point for our hero.
G means gateway - the end of the dungeon (and most propably the enter to another)
# is an obstacle
. is a walkable path.
T is a treasure that can be either mana, health, weapon or spell
E is an enemy that our hero can fight

"""


class Dungeon:
    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]
        self.map = [list(line) for line in lines]

    def print_map(self):
        for line in self.map:
            print(''.join(line))

dungeon = Dungeon("level1.txt")
dungeon.print_map()
