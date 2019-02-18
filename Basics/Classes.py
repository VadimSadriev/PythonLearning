class CountFromBy:

    # something like constructor to init data
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val+= self.incr

    # string representation of object
    def __repr__(self) -> str:
        return str(self.val)


a = CountFromBy(1,2)
a.increase()
print(a.val)
print('type = ', type(a))

print('id = ', id(a))