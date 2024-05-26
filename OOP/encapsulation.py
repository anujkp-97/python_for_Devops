class Base:
    def __init__(self):
        self.a = "I am a value"
        self._c = "I am private c"


b = Base()
print(b.a)
print(b._c)