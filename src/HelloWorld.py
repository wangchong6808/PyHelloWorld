print("hi there!")
print("hi there!")

x = 4
if x==5:
    print("yes")
else:
    print("no")

n = "43"
m = n + "5"
print(m)

x=7.0
y=int(x)
print(x)
print(y)

str='a'
str+='1'
print(str)

print(x,y,x)

name = "John"
age = 23

print("%s is %s years old." % (name, age))

str = "%s is %d, %s a %s" % ("apple",12,"peach","expensive")
print(str)

mylist = [1,2,3]
print("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello"
format_string += " %s %s. Your current balance is $%.2f."
print(format_string % data)

astring = "Hello world!"
print(astring.count("l"))
print(astring[3:7])
print(astring[:])
print(astring[:7:2])

print(astring[::-1])

print(astring.upper())
print(astring.lower())
afewwords = astring.split(" ")
print(afewwords[0])

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")


x = [1,2,3]
y = [1,2,3]
print(x == y)
# Prints out True
print(x is y)


for x in range(5):
    print(x)

for x in range(1,5):
    print(x)

for x in range(10,20,2):
    print(  x  )

count = 0
while count < 6:
    count += 1
    if count % 2 == 0:
        print(count)
    elif count == 5:
        break
    else:
        continue
else:
    print("this is else, count is %d" % count)