import random
from tkinter import *
from tkinter import messagebox
import time


root = Tk()
root.title("Start menu")


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

    def get_coverd_bool(self):
        return self.coverd_bool

    def set_nearby_lava(self, set_lava):
        self.nearby_lava = set_lava

    def set_nears(self, nears):
        self.nears = nears

    def set_button(self, button):
        self.button = button

    def uncovered(self):
        self.coverd_bool = False

    def clicked(self):
        """Calls the clicked function, for some reason it didn't work without this intermediate step
        """
        self.coverd_bool = False
        clicked(
            self)  # Detta ser väldigt underligt ut, jag vet, men det sätt jag ville använda fungerade inte, detta löste problemet


def map_creator(width, height, lava_count):
    """Decides where to put the bombs/lava and what tiles is where, that is to say decides state of each tile and then creates an object of each

    Args:
        width (int): Width of map, amount of items in each row list
        height (int): Height of map, amout of row lists in map
        lava_count (int): Amount of lava/bombs on the map
    """
    x = 0
    y = 0
    lava_list = []
    for i in range(lava_count): lava_list.append(True)
    for i in range(width * height - lava_count): lava_list.append(False)
    random.shuffle(lava_list)
    for row in range(height):
        row_list = []
        for column in range(width):
            lava_bool = lava_list[width * y + x]
            if row == 0:
                if column == 0:
                    state = "top_left"
                elif column == width - 1:
                    state = "top_right"
                else:
                    state = "top"

            elif row == height - 1:
                if column == 0:
                    state = "bot_left"
                elif column == width - 1:
                    state = "bot_right"
                else:
                    state = "bot"

            elif column == 0:
                state = "left"

            elif column == width - 1:
                state = "right"

            else:
                state = "normal"

            row_list.append(
                Tile(lava_bool, x, y, "uncalculated", True, "uncalculated", state, "uncalculated"))
            x += 1
        map.append(row_list)
        y += 1
        x = 0


def calculate_nears():
    """Calculates which Tile objects are within one tile of each
    """

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
                nears = [map[0][x_index - 1], map[0][x_index + 1], map[1][x_index - 1], map[1][x_index],
                         map[1][x_index + 1]]
            elif tile_state == "bot":
                nears = [map[y_index - 1][x_index - 1], map[y_index - 1][x_index], map[y_index - 1][x_index + 1],
                         map[y_index][x_index - 1], map[y_index][x_index + 1]]
            elif tile_state == "left":
                nears = [map[y_index - 1][x_index], map[y_index - 1][x_index + 1], map[y_index][x_index + 1],
                         map[y_index + 1][x_index], map[y_index + 1][x_index + 1]]
            elif tile_state == "right":
                nears = [map[y_index - 1][x_index - 1], map[y_index - 1][x_index], map[y_index][x_index - 1],
                         map[y_index + 1][x_index - 1], map[y_index + 1][x_index]]
            elif tile_state == "normal":
                nears = [map[y_index - 1][x_index - 1], map[y_index - 1][x_index], map[y_index - 1][x_index + 1],
                         map[y_index][x_index - 1], map[y_index][x_index + 1], map[y_index + 1][x_index - 1],
                         map[y_index + 1][x_index], map[y_index + 1][x_index + 1]]
            tile.set_nears(nears)
            x_index += 1
        x_index = 0
        y_index += 1


def calculate_nearby_lava():
    """Calculates how much/many lava/bombs are within one tile
    """

    for row in map:
        for tile in row:
            lava_count = 0
            for near in tile.get_nears():
                if near.get_lava_bool():
                    lava_count += 1
            tile.set_nearby_lava(lava_count)


def big_clear(original_tile):
    """Performs a "big clear". That is to say, when two (or more) tiles with zero nearby lava are next to each other and one is cleard, so is the other.
        If the tile has nearby lava it is clear but the chain reaction, at that tile, goes no further. When done i calls play() to update the map

    Args:
        original_tile (Tile): An object accisiated with the recently clicked button
    """

    big_clear_list = []  # Lista sammankoppalade tiles utan närliggande lava
    latest_list = []
    big_display_list = []  # Lista av alla tiles som ska synas efter processen är klar som har närliggande lava

    for near in original_tile.get_nears():
        if near.get_nearby_lava() == 0:
            big_clear_list.append(near)
            latest_list.append(near)
        else:
            big_display_list.append(near)

    while True:
        if len(latest_list) == 0:  # Om det inte finns något mer all cleara, avbryt loopen
            break
        temp_list = latest_list
        latest_list = []
        for tile in temp_list:
            for near in tile.get_nears():
                if near.get_nearby_lava() == 0 and near not in big_clear_list:
                    big_clear_list.append(near)
                    latest_list.append(near)
                elif near not in big_clear_list:
                    big_display_list.append(near)

    for tile in big_clear_list:
        tile.set_button(Label(root, text="0"))
        tile.uncovered()
    for tile in big_display_list:
        tile.set_button(Label(root, text=tile.get_nearby_lava()))
        tile.uncovered()

    play()


def reset_window():
    """Clears the window by destroying it then and re-creating it
    """
    global root
    root.destroy()  # Följande 3 lines är till för att reseta root fönstret
    root = Tk()
    root.title("Mine Sweeper")


def game_over(mined_lava):
    """Unveils the map and asks if the player wants to restart

    Args:
        mined_lava (Tile): The object associated with the button that lost the game
    """
    for row in map:
        for tile in row:
            if tile.get_lava_bool():
                tile.set_button(Label(root, text="B"))
            else:
                tile.set_button(
                    Label(root, text=tile.get_nearby_lava()))  # fixa sedan så man kan se vilka man lyckades få och inte
    mined_lava.set_button(Label(root, text="B", bg="red"))
    messagebox.showerror("Game Over", "You lost :(\n Click ok to display the uncoverd map")
    play()
    answer = messagebox.askyesno("Restart?", "Would you like to play again?")
    if answer == 1:
        reset_window()
        menu()
    else:
        root.destroy()


def clicked(tile):
    """Defining what happens when tile, the parameter, is clicked

    Args:
        tile (Tile): The Object ascociated with the clicked button
    """
    if tile.get_lava_bool():
        game_over(tile)

    else:
        if tile.get_nearby_lava() != 0:
            tile.set_button(Label(root, text=tile.get_nearby_lava()))  # displayar antal närliggande lava
        else:
            tile.set_button(Label(root, text="0"))
            big_clear(tile)
        play()


def map_render():
    """Defines the button for each Tile object, later to be actually put on the screen
    """
    for row in map:
        for tile in row:
            button = Button(root, width=5, height=2, command=tile.clicked)
            tile.set_button(button)


def game_win():
    answer = messagebox.askyesno("You won!", "You won!")
    if answer:
        messagebox.showinfo("Window for winners", "You are a true pro")
        answer = messagebox.askyesno("Restart?", "Would you like to play again")
    else:
        answer = messagebox.askyesno("You lost u noob!", "Would you like to redeem yourself?")
    if answer:
        reset_window()
        menu()
    else:
        root.destroy()


def play():
    """Updates the playfield
    """

    x = 0
    y = 0
    for row in map:
        for tile in row:
            tile.get_button().grid(row=y, column=x)
            x += 1
            if x >= len(map[0]):
                y += 1
                x = 0
    win = True
    for row in map:
        for tile in row:
            if not tile.get_lava_bool():
                if tile.get_coverd_bool():
                    win = False
    if win:
        game_win()

def menu_confirm(width, height, lava_count):
    """Makes sure the width, height and lavacount (the params) are all valid

    Args:
        width (int): width enterd by the user
        height (int): height enterd by the user
        lava_count (int): amount of lava/bombs enterd by the user
    """
    try:
        width = int(width)
        height = int(height)
        lava_count = int(lava_count)
        if 34 > width > 1 and 21 > height > 1 and 0 != lava_count < height * width:  # Säkerställer användaren skriver in rimliga nummer
            reset_window()
            main(width, height, lava_count)
        elif width > 33: messagebox.showerror("Error", "The (1st) witdh you have enterd is\ntoo big, use a witdh smaller than 34")
        elif height > 20: messagebox.showerror("Error", "The (2nd) height you have enterd is\ntoo big, use a height smaller than 21")
        elif width < 2 or height < 2: messagebox.showerror("Error", "The minimum map size is 2X2\nenter bigger numbers")
        elif lava_count >= height * width: messagebox.showerror("Error", "That is too many mines for your enterd map size")
        else: messagebox.showerror("Error", "Unecpected error")

    except: messagebox.showerror("Error", "Please enter intergers")


def menu():
    """Start menu to decide map size and amount of lava/bombs. When cunfirm_cutton is pressed it calls menu_confirm().
        Each time the function is called it resets the map list.
    """
    global map
    map = []
    confirm_button = Button(root, text="confirm",
                            command=lambda: menu_confirm(width_input.get(), height_input.get(), lava_input.get()))
    width_input = Entry(root)
    height_input = Entry(root)
    lava_input = Entry(root)
    welcome_box = Label(root, text="Welcome!", font=("Arial", 25))
    welcome_text = Label(root,
                         text="Please enter the 1. witdh, 2. height of your\n desired map and you desiered amount of lava/bombs (difficulty)")

    welcome_text.grid(row=0, column=1)
    welcome_box.grid(row=0, column=0)
    width_input.grid(row=1, column=0)
    height_input.grid(row=1, column=1)
    lava_input.grid(row=1, column=2)
    confirm_button.grid(row=1, column=3)


def main(width, height, lava_amount):
    """Function responsible for calling the functions necessary to play the game

    Args:
        width (int): Width of the soon to be created map
        height (int): Height of the soon to be created map
        lava_count (int): Amount of lava/bombs in the soon to be created map
    """
    map_creator(width, height, lava_amount)
    calculate_nears()
    calculate_nearby_lava()
    map_render()
    play()


if __name__ == "__main__":
    menu()
    root.mainloop()

