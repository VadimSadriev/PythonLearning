from flask import session
from functools import wraps

def myFunc(*args):
    # * pre argument means u can pass several parameters
    for a in args:
        print(a, end=' ')
    if args:
        print()


def myFunc2(**kwargs):
    # ** to pass arbitrary numbers of named arguments
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()


def myFunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')

    if kwargs:
        for k, v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You not logged in'
    return wrapper


def decorator_name(func):
    # template for decorators
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.
        # 2. Call decoratod function and return result from that function
        return func(*args, **kwargs)
    # 3. Code to execute instead of decorated function
    return wrapper

myFunc(1, 2, 3, 4)

values = [10, 20, 30, 40]

myFunc(*values)  # pass parameters with * means func will seperate list into several objects



myFunc2(a=10, b=20)

dict = {'name': 'Alex', 'age': '10'}

myFunc2(**dict)



