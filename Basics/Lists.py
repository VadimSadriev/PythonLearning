vowels = ["a", "e", "i", "o", "u"]

# word = input("Provide a word to search for vowels: ")
word = "Williways"
found = []
for letter in word:
    if letter in vowels:
        if not found.__contains__(letter):
            found.append(letter)

for letter in found:
    print(letter)


nums = [1,2,3]

nums.extend([5,6])
print(nums)

nums.pop()
print(nums)

nums.insert(0, 24)
print(nums)

phrase = "dont panic"
plist = list(phrase)

print(phrase)
print(plist)

first = [1, 2, 3, 4]
second = first

# when asign to variable you set reference to object not actual object so use copy to get another object
third = second.copy()
second.append(6)
print(first)
print(second)
print(third)

word = "Hello world"

letter = list(word)

print(letter[0:10:3])
print(letter[3:])
print(letter[:10])
print(letter[::2])

print(",".join(["privet", "Mir"]))

print(word[::-1])  # backwords
