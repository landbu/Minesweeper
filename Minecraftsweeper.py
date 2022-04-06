import random


map = []


class Tile:
    def __init__(self, lava_bool: bool, x_cord, y_cord, nearby_lava):
        self.lava_bool = lava_bool
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.nearby_lava = nearby_lava

    def get_lava_bool(self):
        return self.lava_bool

    def get_position(self):
        return [self.x_cord, self.y_cord]

    def set_nearby_lava(self, set_lava):
        self.nearby_lava = set_lava


def map_creator(width, height):
    x = 0
    y = 0
    for row in range(height):
        for column in range(width):
            lava_bool = random.choice([True, False, False, False, False]) #Justera sannolikheten senare
            nearby_lava = "Uncalculated"
            map.append(Tile(lava_bool, x, y, nearby_lava))
            x += 1
        y += 1
        x = 0

map_creator(5, 5)


def main():
    print("Welcome to main!")
    map_creator(int(input("Width of map: ")), int(input("height of map: ")))
    for i in map:
        print(i.get_position())
        print(i.get_lava_bool())


if __name__ == "__main__":
    main()