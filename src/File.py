import os
import fileinput

filePath = './data.txt'
filePath1 = './data1.txt'
largeFile = '/Users/wangchong/Documents/Benz/OTR/AS/Database/otr_vehicle_uat.sql'

f = open(filePath, 'w')

f.write("hello world! \n How are you ?")
f.close()

r = open(filePath, 'r')
print("file content is ", r.read())

r = open(largeFile, 'r')
for line in r:
    print(line)

r.close()

print('this is iterating with input')
for line in fileinput.input(largeFile):
    print(line)


os.rename(filePath, filePath1)

os.remove(filePath1)
