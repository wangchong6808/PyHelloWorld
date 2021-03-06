# game.py
# import the draw module


import draw
from draw import clear_screen

from store import add_role
import sys
import modules.base.goods


def play_game():
    return "this is the game's name"


def print_role():
    print(draw.roles)


def main():
    result = play_game()
    draw.draw_game(result)
    clear_screen(result)
    print_role()
    add_role()
    print_role()
    print(sys.path)



# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
