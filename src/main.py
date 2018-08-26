# game.py
# import the draw module


import sys
import modules.mygame.store as store
import modules.mygame.draw as draw


def play_game():
    return "this is the game's name"


def print_role():
    print(1)


def main():
    result = play_game()
    print_role()
    print_role()
    store.add_role()
    print(draw.roles)
    print(sys.path)


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
