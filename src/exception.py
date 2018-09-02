def divide(n, m):
    try:
        x = n / m
        print('result is', x)
    except ZeroDivisionError:
        print('something wrong happend')


divide(100, 10)
divide(100, 0)
