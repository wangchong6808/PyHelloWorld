
def playMusic(instrument, song):
    print("I am playing %s to express '%s'" % (instrument,  song))
    return 'success'


outcome = playMusic('piano', 'yesterday once again')
print('outcome is %s' % outcome)


class Animal:

    name = None
    size = 20
    hasTail = False

    def shout(self):
        print("I am a %s, I am %d centimeters long and I %s have tail ?. " % (self.name, self.size, self.mytail()))

    def mytail(self):
        if self.hasTail:
            return ''
        else:
            return "don't"


dog = Animal()
dog.name = 'Dog'
dog.shout()
