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