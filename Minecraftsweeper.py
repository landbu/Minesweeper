import random
from tkinter import *
from tkinter import messagebox
import time

root = Tk()
root.title("Start menu")
map = []
map_list = []


class Tile:
    def __init__(self, lava_bool: bool, x_cord, y_cord, nearby_lava, coverd_bool: bool, nears, state, button,
                 prime_nears):
        self.lava_bool = lava_bool
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.nearby_lava = nearby_lava
        self.coverd_bool = coverd_bool
        self.nears = nears
        self.state = state
        self.button = button
        self.prime_nears = prime_nears

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

    def set_prime_nears(self, prime_nears):
        self.prime_nears = self.prime_nears

    def clicked(self):
        self.coverd_bool = False
        clicked(
            self)  # Detta ser väldigt underligt ut, jag vet, men det sätt jag ville använda fungerade inte, detta löste problemet


def map_creator(width, height):
    x = 0
    y = 0
    for row in range(height):
        row_list = []
        for column in range(width):
            lava_bool = random.choice([True, False, False, False, False])  # Justera sannolikheten senare

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
                Tile(lava_bool, x, y, "uncalculated", True, "uncalculated", state, "uncalculated", "uncalculated"))
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


def calculate_prime_nears():
    for tile in map:
        if tile.get_nearby_lava() == 0:
            state = tile.get_state()
            if state == "top_left":
                tile.set_prime_nears([tile.get_nears()[0], tile.get_nears()[1]])
            elif state == "top":
                tile.set_prime_nears([tile.get_nears()[0], tile.get_nears()[1]], tile.get_nears()[3])
            elif state == "top_right":
                tile.set_prime_nears([tile.get_nears()[0], tile.get_nears()[2]])
            elif state == "left":
                tile.set_prime_nears([tile.get_nears()[0], tile.get_nears()[2], tile.get_nears()[3]])
            elif state == "normal":
                tile.set_prime_nears(
                    [tile.get_nears()[1], tile.get_nears()[3], tile.get_nears()[4], tile.get_nears()[6]])
            elif state == "right":
                tile.set_prime_nears(
                    [tile.get_nears()[1], tile.get_nears()[2], tile.get_nears()[0], tile.get_nears()[4]])
            elif state == "bot_left":
                tile.set_prime_nears([tile.get_nears()[0], tile.get_nears()[2]])
            elif state == "bot_right":
                tile.set_prime_nears([tile.get_nears()[1], tile.get_nears()[2]])


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
    # funktionen ansvarar för att göra de stora clearsen

    big_clear_list = []  # Lista sammankoppalade tiles utan nrliggandelava
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
    for tile in big_display_list:
        tile.set_button(Label(root, text=tile.get_nearby_lava()))
    play()


def reset_window():
    global root
    root.destroy()  # Följande 3 lines är till för att reseta root fönstret
    root = Tk()
    root.title("Mine Sweeper")


def game_over(mined_lava):
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
    else: root.destroy()


def clicked(tile):
    """
    Definerar vad som händer när en knapp blir tryckt
    """
    if tile.get_lava_bool():
        game_over(tile)

    else:
        if tile.get_nearby_lava() != 0:
            tile.set_button(Label(root, text=tile.get_nearby_lava()))  # displayar antal närliggande lava
        else:
            big_clear(tile)
        play()


def map_render(width):
    for row in map:
        for tile in row:
            map_list.append(tile)
    for tile in map_list:
        button = Button(root, width=5, height=2, command=tile.clicked)
        tile.set_button(button)


def play():
    x = 0
    y = 0
    for tile in map_list:
        tile.get_button().grid(row=y, column=x)
        x += 1
        if x >= len(map[0]):
            y += 1
            x = 0


def menu_confirm(width, height):
    try:
        width = int(width)
        height = int(height)
        if 34 > width > 1 and 21 > height > 1:  # Säkerställer användaren skriver in rimliga nummer
            reset_window()
            #global root
            #root.destroy()  # Följande 3 lines är till för att reseta root fönstret
            #root = Tk()
            #root.title("Mine Sweeper")
            main(width, height)
        elif width > 33:
            messagebox.showerror("Error", "The (1st) witdh you have enterd is\ntoo big, use a witdh smaller than 34")
        elif height > 20:
            messagebox.showerror("Error", "The (2nd) height you have enterd is\ntoo big, use a height smaller than 21")
        elif width < 2 or height < 2:
            messagebox.showerror("Error", "The minimum map size is 2X2\nenter bigger numbers")
        else:
            messagebox.showerror("Error", "Unecpected error")

    except:
        messagebox.showerror("Error", "Please enter intergers")


def menu():
    confirm_button = Button(root, text="confirm", command=lambda: menu_confirm(width_input.get(), height_input.get()))
    width_input = Entry(root, text="test")
    height_input = Entry(root)
    welcome_box = Label(root, text="Welcome!", font=("Arial", 25))
    welcome_text = Label(root, text="Please enter the 1. witdh and \n2. height of your desired map")

    welcome_text.grid(row=0, column=1)
    welcome_box.grid(row=0, column=0)
    width_input.grid(row=1, column=0)
    height_input.grid(row=1, column=1)
    confirm_button.grid(row=1, column=2)


def main(width, height):
    map_creator(width, height)
    calculate_nears()
    calculate_nearby_lava()
    # calculate_prime_nears() jag tror faktiskt inte detta behövs
    map_render(width)
    play()


if __name__ == "__main__":
    menu()
    root.mainloop()
