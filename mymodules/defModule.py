def search4vowels():
    """Ouput is vowels found in word"""
    vowels = set('aeiou')
    word = input("Provde a word to search for vowels = ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


def search4vowels(phrase: str) -> set:
    """Output is vowels found in word"""
    vowels = set('aeiou')
   # return bool(vowels.intersection(set(word)))
    return vowels.intersection(set(phrase))


def search4letter(phrase: str, letters: str = 'aeiou') -> set:
    """Returns set of letters from 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))


def double(arg: float):
        print('before: ', arg)
        arg = arg*2
        print('after: ', arg)


def change(arg: list) -> list:
        print('before: ', list)
        list.append('MoreData')
        print('after: ', list)


