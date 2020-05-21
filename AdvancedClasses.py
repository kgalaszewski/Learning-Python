# Enumerations 
from enum import Enum

class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4

print(Fruit.APPLE) # Fruit.APPLE
print(type(Fruit)) # class enum.EnumMeta
print(type(Fruit.APPLE)) # enum 'Fruit'
print(repr(Fruit.APPLE)) # canonical string representation of an object
print(Fruit.APPLE.name) # Apple
print(Fruit.APPLE.value) # 1 


# Class String functions - all of them can be overloaded
class SomeClass:
    pass

obj = SomeClass()
repr(obj) # obj.__repr__ # repr should contain useful info for debugging, dict like info
str(obj) # obj.__str__ # should store nice readable info
format(obj) # obj.__format__ # should store nice readable info
bytes(obj) # obj.__bytes__ # should contain info encoded in utf-8


# Class Numerical Operators to override
# regular numeric functions
# __add__ czyli +
# __sub__ czyli -
# __mul__ czyli *
# __div__ czyli /
# __floordiv__ czyli //
# __pow__ czyli **
# __and__ czyli and (&&)
# __or__ czyli or (||)
# shorten versions of numeric functions
# __iadd__ czyli +=
# __isub__ czyli -=
# __imul__ czyli *=
# __idiv__ czyli /=
# __ifloordiv__ czyli //=
# __ipow__ czyli **=
# __iand__ czyli and (&&=)
# __ior__ czyli or (||=)


# !!!!!!!!!!!!!!!!!!
# Dzieki nadpisaniu >= > <= < itd nasz obiekt moze byc sortowany
# Normalnie w liscie naszych obiektow customowych nie mozesz dac sort na liscie
# ale przy ich nadpisaniu mozesz posortowac


