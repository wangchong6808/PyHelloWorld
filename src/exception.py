class MyError(Exception):

    def __str__(self):
        return 'this is my error'


def divide(n, m):
    try:
        x = n / m
        print('result is', x)
    except (ZeroDivisionError, NameError) as e:
        print('something wrong happend', e)
    except SyntaxError:
        print('syntax error')
    else:
        print('no error happened')
    finally:
        print('program is finished')


def raise_my_error(m):
    try:
        print('m is', m)
        raise MyError()
    except MyError as e:
        print('the error is ', e)


# try else finally
divide(100, 10)
# try except finally
divide(100, 0)

raise_my_error('')
