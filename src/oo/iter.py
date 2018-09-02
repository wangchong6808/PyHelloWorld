class Fib(object):

    def __init__(self):

        self.age = 13
        self.a, self.b = 0, 1
        self.c, self.d = 1, 1

    def __iter__(self):
        print('iter', self.c)
        self.c += 1

        return self

    def __next__(self):
        print('next', self.d)
        self.a, self.b = self.b, self.a + self.b
        self.d += 1
        if self.d > 20:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        a, b = 1, 1
        for i in range(item):
            a, b = b, a+b
        return a

    def __getattr__(self, item):
        if item == 'name':
            return 'undefined'
        if item == 'age':
            return 15

    def __call__(self, *args, **kwargs):
        print('this is call method', args)


class nocall(object):
    pass

# 因为实现了__iter__ 和__next__方法 所以可以用for循环做迭代
for i in Fib():
    print(i)

b = Fib()

# 因为实现了__getitem__方法  所以可以像数组一样按照下标获取某一个数据
print(b[10])

# name并未明确定义所以使用了__getattr__方法获取值，而age有明确定义的属性则没有调用__getattr__获取值
print(b.name)
print(b.age)
print(b.gender)

# 之所以可以将对象当做函数一样调用是因为对象定义了__call__方法，这样表面看来就很难区分是对象还是函数了，实际上对象和函数本质上没什么区别，通过callable方法可以判断一个变量是否是可以被调用的
b()
b('a')

print(callable(b))

c = nocall()
print(callable(c))
