import sys

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)


try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing')
except PermissionError:
    print('You have no rughs')
except Exception as err:
    print("some other rro occured", str(err))

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except Exception as err:
    print("some other error occured", str(err))
