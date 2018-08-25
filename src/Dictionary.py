phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
phonebook["Tome"] = 45673464
del phonebook['John']

for key, value in phonebook.items():
    print(key, value)

names = []
names.append('a')
names.append('b')
names.remove('b')
for item in names:
    print(item)