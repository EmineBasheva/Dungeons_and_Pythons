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
import itertools


class Dungeon:
    def __init__(self, filename):
        lines = open(filename).read().split("\n")
        lines = [line for line in lines if line.strip() != ""]

        self.map = [list(line) for line in lines]

        self.spawn_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line) if ch == "S"]

        self.treasure_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line) if ch == "T"]

        self.enemy_points = [[i, j] for i, line in enumerate(self.map)
                             for j, ch in enumerate(line) if ch == "E"]

        self.obstacle_points = [[i, j] for i, line in enumerate(self.map)
                                for j, ch in enumerate(line) if ch == "#"]

        self.curr_pos = [None, None]

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def spawn(self):
        if self.spawn_points is not list():
            self.map[self.spawn_points[0][0]][self.spawn_points[0][1]] = "H"
            self.curr_pos = [self.spawn_points[0][0], self.spawn_points[0][1]]
            del self.spawn_points[0]
            return True
        else:
            return False

    def point_in_dungeon(self, point):
        if point[0] < 0 or point[1] < 0:
            return False
        elif point[0] > len(self.map[0]) or point[1] > len(self.map):
            return False
        return True

    def swap_curr_point_with(self, point):
        if point in self.obstacle_points:
            return False
#NEED TO FINISH THIS SHIT!
        if point in self.treasure_points:
            self.map[self.curr_pos[0]][self.curr_pos[1]] = "."
            self.map[point[0]][point[1]] = "H"
            self.curr_pos[0], self.curr_pos[1] = point[0], point[1]
        if self.point_in_dungeon(point):
            self.map[self.curr_pos[0]][self.curr_pos[1]], self.map[point[0]][point[1]] = self.map[point[0]][point[1]], self.map[self.curr_pos[0]][self.curr_pos[1]]
            self.curr_pos[0], self.curr_pos[1] = point[0], point[1]
        else:
            return False

    def move_hero(self, direction):
        point = []
        if direction is "up":
            point.append(self.curr_pos[0] - 1)
            point.append(self.curr_pos[1])
            return self.swap_curr_point_with(point)
        if direction is "down":
            point.append(self.curr_pos[0] + 1)
            point.append(self.curr_pos[1])
            return self.swap_curr_point_with(point)
        if direction is "right":
            point.append(self.curr_pos[0])
            point.append(self.curr_pos[1] + 1)
            return self.swap_curr_point_with(point)
        if direction is "left":
            point.append(self.curr_pos[0])
            point.append(self.curr_pos[1] - 1)
            return self.swap_curr_point_with(point)


dungeon = Dungeon("level1.txt")
dungeon.print_map()
dungeon.spawn()
dungeon.print_map()
dungeon.move_hero("right")
dungeon.move_hero("down")
dungeon.print_map()
print(dungeon.curr_pos)