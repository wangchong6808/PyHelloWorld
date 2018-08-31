#! /usr/bin/python3
#-*-coding:UTF-8-*-

list1 = ['a', 'b', 'c']
for c in list1:
    print(c)

dic1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for entry in dic1.items():
    print(entry)

# 序列解包
for k, v in dic1.items():
    print(k, v)

for i in range(1, 10):
    print(i)

key = ['key1', 'key2']
value = ['value1', 'value2', 'value3']

matrix = []

for k, v in zip(key, value):
    print(k, v)

for k in key:
    for v in value:
        matrix.append((k, v))


print(matrix)

list1 = ['a', 'c', 'b']
list1.reverse()
print(list1)
print(list(reversed('abc')))
print(sorted(list1))

for c in reversed('abc'):
    print(c)
