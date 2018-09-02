# game.py
# import the draw module


import sys
import modules.mygame.store as store
import modules.mygame.draw as draw


def play_game():
    return "this is the game's name"


def print_role():
    print(1)


def set_value():
    a, b, c = 1, 2, 3
    print(a, b, c)
    c, a, b = a, b, c
    print(a, b, c)

    nums = 1, 2, 3
    print(nums)


def translate():
    str = "just do it or never do it!"
    init = "ot"
    rep = "0T"
    trans = "".maketrans(init, rep)
    print(str.translate(trans))


def main():
    result = play_game()
    print_role()
    print_role()
    store.add_role()
    print(draw.roles)
    print(sys.path)
    set_value()
    translate()


# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
