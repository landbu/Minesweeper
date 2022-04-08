import random

map = []


class Tile:
    def __init__(self, lava_bool: bool, x_cord, y_cord, nearby_lava, coverd_bool: bool, nears, state):
        self.lava_bool = lava_bool
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.nearby_lava = nearby_lava
        self.coverd_bool = coverd_bool
        self.nears = nears
        self.state = state


    def get_lava_bool(self):
        return self.lava_bool

    def get_position(self):
        return [self.x_cord, self.y_cord]

    def set_nearby_lava(self, set_lava):
        self.nearby_lava = set_lava

    def set_nears(self, nears):
        self.nears = nears

    def get_state(self):
        return self.state

    def get_nears(self):
        return self.nears

def map_creator(width, height):
    x = 0
    y = 0
    for row in range(height):
        row_list = []
        for column in range(width):
            lava_bool = random.choice([True, False, False, False, False]) #Justera sannolikheten senare

            if row == 0:
                if column == 0:
                    state = "top_left"
                elif column == width-1:
                    state = "top_right"
                else:
                    state = "top"

            elif row == height-1:
                if column == 0:
                    state = "bot_left"
                elif column == width-1:
                    state = "bot_right"
                else:
                    state = "bot"

            elif column == 0:
                state = "left"

            elif column == width-1:
                state = "right"

            else:
                state = "normal"

            row_list.append(Tile(lava_bool, x, y, "uncalculated", True, "uncalculated", state))
            x += 1
        map.append(row_list)
        y += 1
        x = 0


def calculate_nears():
    x_index = 0
    y_index = 0
    for row in map:
        for tile in row:
            tile_state = tile.get_state()
            if tile_state == "top_left":
                nears = [map[0][1], map[1][0], map[1][1]]
            elif tile_state == "top_right":
                nears = [map[-2][0], map[-1][1], map[-2][1]]
            elif tile_state == "bot_left":
                nears = [map[0][-2], map[1][-2], map[1][-1]]
            elif tile_state == "bot_right":
                nears = [map[-2][-2], map[-1][-2], map[-2][-1]]
            elif tile_state == "top":
                nears = [map[x_index-1][0], map[x_index+1][0], map[x_index-1][1], map[x_index][1], map[x_index+1][1]]
            elif tile_state == "bot":
                nears = [map[x_index-1][y_index-1], map[x_index][y_index-1], map[x_index+1][y_index-1], map[x_index-1][y_index], map[x_index+1][y_index]]
            elif tile_state == "left":
                nears = [map[x_index][y_index-1], map[x_index+1][y_index-1], map[x_index+1][y_index], map[x_index][y_index+1], map[x_index+1][y_index+1]]
            elif tile_state == "right":
                nears = [map[x_index-1][y_index-1], map[x_index][y_index-1], map[x_index-1][y_index], map[x_index-1][y_index+1],map[x_index][y_index+1]]
            elif tile_state == "normal":
                nears = [map[x_index-1][y_index-1], map[x_index][y_index-1], map[x_index+1][y_index-1], map[x_index-1][y_index], map[x_index+1][y_index], map[x_index-1][y_index+1], map[x_index][y_index+1], map[x_index+1][y_index+1]]
            tile.set_nears(nears)
            x_index += 1
        x_index = 0
        y_index +=1
def calculate_nearby_lava():
    # Räkna ut hur många minor som ligger nära med hjälp av nears atributet som räknas ut i calculate_nears()
    pass


def basic_print(var):
    if var == "pos":
        for row in map:
            for obj in row:
                print(obj.get_position(), end="")
            print("")

    elif var == "state":
        for row in map:
            for obj in row:
                print(obj.get_state(), end=", ")
            print("")


def main():
    print("Welcome to main!")
    map_creator(int(input("Width of map: ")), int(input("height of map: ")))
    calculate_nears()
    for row in map:
        for i in row:
            for p in i.get_nears():
                print(p)





if __name__ == "__main__":
    main()
