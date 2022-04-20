import random
from tkinter import *


root = Tk()
root.title("Mine Sweeper")
map = []
map_list = []


class Tile:
    def __init__(self, lava_bool: bool, x_cord, y_cord, nearby_lava, coverd_bool: bool, nears, state, button):
        self.lava_bool = lava_bool
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.nearby_lava = nearby_lava
        self.coverd_bool = coverd_bool
        self.nears = nears
        self.state = state
        self.button = button


    def get_lava_bool(self):
        return self.lava_bool

    def get_position(self):
        return [self.x_cord, self.y_cord]

    def get_state(self):
        return self.state

    def get_nears(self):
        return self.nears

    def get_nearby_lava(self):
        return self.nearby_lava

    def get_button(self):
        return self.button

    def set_nearby_lava(self, set_lava):
        self.nearby_lava = set_lava

    def set_nears(self, nears):
        self.nears = nears

    def set_button(self, button):
        self.button = button

    def clicked(self):
        self.coverd_bool = False
        clicked(self) # Detta ser väldigt underligt ut, jag vet, men det sätt jag ville använda fungerade inte, detta löste problemet



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

            row_list.append(Tile(lava_bool, x, y, "uncalculated", True, "uncalculated", state, "uncalculated"))
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
                nears = [map[0][-2], map[1][-2], map[1][-1]]
            elif tile_state == "bot_left":
                nears = [map[-2][0], map[-2][1], map[-1][1]]
            elif tile_state == "bot_right":
                nears = [map[-2][-2], map[-2][-1], map[-1][-2]]
            elif tile_state == "top":
                nears = [map[0][x_index-1], map[0][x_index+1], map[1][x_index-1], map[1][x_index], map[1][x_index+1]]
            elif tile_state == "bot":
                nears = [map[y_index-1][x_index-1], map[y_index-1][x_index], map[y_index-1][x_index+1], map[y_index][x_index-1], map[y_index][x_index+1]]
            elif tile_state == "left":
                nears = [map[y_index-1][x_index], map[y_index-1][x_index+1], map[y_index][x_index+1], map[y_index+1][x_index], map[y_index+1][x_index+1]]
            elif tile_state == "right":
                nears = [map[y_index-1][x_index-1], map[y_index-1][x_index], map[y_index][x_index-1], map[y_index+1][x_index-1],map[y_index+1][x_index]]
            elif tile_state == "normal":
                nears = [map[y_index-1][x_index-1], map[y_index-1][x_index], map[y_index-1][x_index+1], map[y_index][x_index-1], map[y_index][x_index+1], map[y_index+1][x_index-1], map[y_index+1][x_index], map[y_index+1][x_index+1]]
            tile.set_nears(nears)
            x_index += 1
        x_index = 0
        y_index +=1


def calculate_nearby_lava():
    # Räknar ut hur mycket lava som ligger nära med hjälp av nears atributet som räknas ut i calculate_nears()
    for row in map:
        for tile in row:
            lava_count = 0
            for near in tile.get_nears():
                if near.get_lava_bool():
                    lava_count += 1
            tile.set_nearby_lava(lava_count)


def big_clear(original_tile):
    big_clear_list = [] # Lista sammankoppalade tiles utan nrliggandelava
    latest_list = []
    big_display_list = [] # Lista av alla tiles som ska synas efter processen är klar som har närliggande lava

    for near in original_tile.get_nears():
        if near.get_nearby_lava() == 0:
            big_clear_list.append(near)
            latest_list.append(near)
        else:
            big_display_list.append(near)
    while True:
        if len(latest_list) == 0:
            break
        for tile in latest_list:
            latest_list = []
            for near in tile:
                if near.get_nearby_lava() == 0:
                    big_clear_list.append(near)
                    latest_list.append(near)
                else:
                    big_display_list.append(near)

    for tile in big_clear_list:
        # tile.set_button(bla bla) # Här var du senast


def clicked(tile):
    """
    Definerar vad som händer när en knapp blir tryckt
    """
    if tile.get_lava_bool():
        tile.set_button(Label(root, text="B"))
    else:
        if tile.get_nearby_lava() != 0: tile.set_button(Label(root, text=tile.get_nearby_lava())) #displayar antal närliggande lava
        else: big_clear(tile)
    play(len(map[0]))


def map_render(width):
    for row in map:
        for tile in row:
            map_list.append(tile)
    for tile in map_list:
        #button = Button(root, width=5, height=2, command=lambda: clicked(tile))
        button = Button(root, width=5, height=2, command=tile.clicked)
        tile.set_button(button)


def play(width):
    x = 0
    y = 0
    for tile in map_list:
        tile.get_button().grid(row=y, column=x)
        x += 1
        if x >= width:
            y += 1
            x = 0


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

    elif var == "lava":
        for row in map:
            for obj in row:
                if obj.get_lava_bool(): print("1", end=", ")
                else: print("0", end=", ")
            print("")


def main():
    print("Welcome to main!")
    width = int(input("Width of map: "))
    height = int(input("height of map: "))
    map_creator(width, height)
    calculate_nears()
    calculate_nearby_lava()
    map_render(width)
    play(width)

    root.mainloop()


if __name__ == "__main__":
    main()
