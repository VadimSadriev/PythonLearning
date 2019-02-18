import defModule

print(defModule.search4vowels('sky'))
print(defModule.search4letter('sky', 'aiy'))
print(defModule.search4letter(letters='lol', phrase='sky'))

l = list()
print('list =', l)

l = [1, 2, 3]
print('list =', l)

d = dict()
print('dict =', d)

d = {'first': 1, 'second': 2}
print('dict = ', d)

s = set()
print('set = ', s)
s = {1, 2, 3}
print('set = ', s)

t = tuple()
print('tuple =', t)

t = (1, 2, 3)
print('tuple =', t)
help(defModule.search4vowels)

num = 10
defModule.double(num)

saying = 'hello'
defModule.double(saying)
print(saying)

numbers = [42, 256, 16]
defModule.change(numbers)
print(numbers)