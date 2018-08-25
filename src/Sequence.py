mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist[2:9])
print(mylist[-5:-8:-1])
print(mylist[10:5:-2])

list1 = [12, 13]

print(mylist + list1)

list2 = [1, "1", 2, "2"]
print(list1 + list2)

mylist = list('hi,')
print(mylist)

mylist[1:] = list('ello')
print(mylist)

mylist = list('这是一辆车的轮胎')
mylist[4:4] = ['GLE', '奔', '驰']
print(mylist)

mylist = list('这是一辆车的轮胎')
mylist[4:4] = list('GLE奔驰')
print(mylist)

mylist[4:9] = []
print(mylist)


def add(x, y):
    return x + y


print(add(10, 99))

mixed_list = [[1, 2, 3], ['1', '2', '3'], [1, 2, 3]]
num_list = [1, 2, 3]
print(mixed_list.count(num_list))

mixed_list.extend([[5, 6, 7]])
print(mixed_list)

a = [1, 2]
b = [3, 4]
print(a + b)
print(a)
a.extend(b)
print(a)
a[len(a):] = b
print(a)
a[len(a) - 1:len(a) - 1] = b
print(a)

print(a.index(3))
# print(a.index(5))  error
a.insert(2, 5)
print(a)

stack = [1, 2, 3, 4]
print(stack.pop())
print(stack)
del stack[2]
print(stack)

stack.remove(1)
# stack.remove(3)  error
print(stack)

stack = [1, 2, 3, 4]
stack.pop()
print(stack)

stack = [1, 3, 4, 2]
stack1 = []
stack1[:] = stack
stack1.sort()
print(stack)
print(stack1)

stack = ['1', '32', '4', '2']
stack1 = stack.copy()
stack1.sort()
stack1.sort(key=len, reverse=True)
print(stack)
print(stack1)
