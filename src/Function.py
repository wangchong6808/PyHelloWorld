from functools import partial


def playMusic(instrument, song):
    print("I am playing %s to express '%s'" % (instrument, song))
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


def multi_param(p1, p2=10, *p3, **p4):
    print('p1', p1)
    print('p2', p2)
    for p in p3:
        print('p3', p)
    for k, v in p4.items():
        print('p4', 'k:%s v:%s' % (k, v))


multi_param('hi', 2, 3, 4, 5, name=11)


def recurse(n):
    if n <= 1:
        return 1
    return n * recurse(n - 1)


def cal_multi(n, m):
    if n <= 1:
        return m
    return cal_multi(n - 1, n * m)


def recurse_tail(n):
    if n <= 1:
        return 1
    return cal_multi(n - 1, n)


print(recurse(6))
print(recurse_tail(6))


def multiply(m, n):
    return m * n


# 通过偏函数做柯里化
fixed_multi = partial(multiply, 100)
x = fixed_multi(20)
print(x)
