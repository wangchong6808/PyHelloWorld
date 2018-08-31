def cal(n):
    if n <= 1:
        return n
    return n * cal(n - 1)


print('8的阶乘是', cal(8))


def cal_lazy(n):
    def cal1(i):
        def cal2():
            return i * i

        return cal2

    ret = []
    for j in range(1, n + 1):
        ret.append(cal1(j))
    return ret


def cal_lazy1(n):
    ret = []
    for i in range(1, n + 1):
        def cal1():
            return i * i

        ret.append(cal1)
    return ret


print('直接引用循环变量：')
funcs = cal_lazy1(3)
for func in funcs:
    print(func())

print('将循环变量作为实参传给形参：')
funcs = cal_lazy(3)
for func in funcs:
    print(func())

name = 'jack'


def change_global_name(p):
    global name
    name = p


def change_local_name(p):
    name = p


def lazy_change_global_name(p):
    def change():
        global name
        name = p

    return change


change_local_name('tom')
print('函数local变量没有导致全局变量修改', name)

change_global_name('tom1')
print('使用global标记后可以修改全局变量', name)

ret = lazy_change_global_name('tom2')
print('调用返回函数前', name)
ret()
print('调用返回函数后', name)


def change_by_inner_func(p):
    outter = 1

    def inner():
        # inner = outer  这句编译不过，无法直接访问外部函数的局部变量
        innervalue = p
        outter = 2

    inner()
    print('通过内部函数修改外部函数的变量', outter)


change_by_inner_func(3)