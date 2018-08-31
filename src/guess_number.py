import random

count = 1
answer = random.randint(0, 100)

while True:
    print('this is the %s guess' % count)
    count += 1
    input_value = int(input('please guess:'))
    if input_value > answer:
        print('it is big')
    elif input_value < answer:
        print('it is small')
    else:
        print('that is correct')
        break
