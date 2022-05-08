# Minecraftsweeper

## Description 
A simple minecrafty twist on the classic minesweerper with blocks to be mined and lava to be avoided. In later versions I hope to introduce further
elements to seperate it from the classic minesweerper


## Built with


- All code: Python
- Graphics - Tkinter python library 

## Requirements/Prerequisites

***Vad krävs för att köra ditt program? Lista bara kraven.***

- Python 3.7+

## Installation

The program is tested and made for python 3+ (made in 3.10.2), to install python follow [this](https://www.python.org/downloads/) link. No further istalls are recuired to run the program 

## Code conventions

pep-8

## How to play (Usage)

By starting the program the user will be presented with a menu. In the menu the user cna specify information about the game he wants to play, height of the map, leangh and amount of lava on the map. After that the game consists of clicking on calculated tiles to uncover the map. If a lava tile is clicked the game is lost and if all but the lava tiles are cleared the game is win


## Example (exempelkörning)

image.png

## To do/Roadmap

- [x] Publish a functional, but minimalistic, minesweeper copy
- [ ] Add the missing minesweeper elements (mainly flags, but also perhaps highscore)
- [ ] Use graphics to make it look like a minecraft mine
- [ ] Add aditional content to the game, like special ores to mine and (the option make) bigger maps.
- [ ] Defeat Gustav Brandeel in the best minesweeper contest



## Changelog


### Version 0.1.0

#### Added or changed

- Added "Tile" class
- Added the map creator function to create a grided map of Tile objects and also randomly place lava (bombs in classical minesweeper).
- Added simple main/menu to call map_creator with inputed args



### Version 0.2.0

#### Added or changed
- Adeed a function, calculate_nears(), that calculates and asigns each Tile object thier nearby, within a leangh of one on the map, Tile objects
- Added a (later to be romved) function to more easly verify the succes of newly added functions by printing the entire map in a desired manner, which possition it has, how many nearby lava (when that is added) ect.


### Version 0.3.0

#### Added or changed
- Added a function, calcucalte_nearby_lava(), to, based on the previsously calculated nearby objects, asign the object with the amount of objects in its "near" atribute with the lava_bool atribute set to True
- Changed the Tile class to include a button atribute so that each tile -object will get its own ascociated button
- Added the clicked() function to define what happens when a button is clicked
- Added a tkinter window that displays each button


### Version 0.4.0
#### Added or changed
- Added the big_clear() function to do the multi-clears one should be familiar with from classical minesweeper
- Added the calculate_prime_nears to calculate which of each objects nears are not near by diagonals. This will later be used to improve upon the big clears. The prime_nears also became an atribute of each object


#### Removed
- Removed the basic_print() function because I now longer thought it helpful in bug testing or any testing at all.


### Version 0.4.1

#### Added or changed
- Fixed a bug with big_clear
- Added some long-needed comments
#### Removed
- Removed all of the prime_nears stuff, simple decided I didn't feel the concept neccisary 


### Version 0.5.0

#### Added or changed
- Added a game_over() function so that the player actually looses when clicking on a lava infested tile/block
- Added a proper, tkinter, menu and a function that make sures the entered height and width are valid inputs
- Cleaned up the code a bit


### Version 1.0.0
#### Added or changed
- Improved the look of the menu
- Made it possible to actually win the game
- Added the option of how many mines the player wants into the menu
- Added proper docstrings
- Cleaned up the code further

## Contribute

### When to help
Currently no changes/help is premitted, the project is not yet graded. 
### What to help with
When graded, help will be welcomed in improving the UI, the menu for example is currently quite clunky- looking.
### How to propose changed
Do a pull request and add and dm me on disc or just mail me


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Contact


Adam Landbü - Discord: Boofen#8389 - Mail: adam.landbu@gmail.com

Link to project: https://github.com/landbu/Minesweeper

## Acknowledgments

***Här kan du lista resurser eller personer som har hjälpt dig med projektet. Det kan vara länkar till tutorials eller dokumentation, eller bara någon annans profil som du vill uppmärksamma. Har du inget som behöver tas här så kan du strunta i rubriken. ***

- Nicklas Lund
- [This guy](https://www.youtube.com/watch?v=YXPyB4XeYLA&t=9024s)
- [Stack-Overflow](https://stackoverflow.com/)
