vowels = {'a', 'b', 'e', 'e', 'i', 'u', 'u'}
print('vowels = ',vowels)

vowels2 = set('abeeiuu')
print('vowels2 = ',vowels2)

vowels3 = set('aeiou')
word = 'hello'

print('vowels3 = ', vowels3)

u = sorted(vowels3.union(set(word)))
print('union = ', u)

d = vowels3.difference(set(word))
print('difference = ', d)

i = vowels3.intersection(set(word))
print('intersection = ', i)




