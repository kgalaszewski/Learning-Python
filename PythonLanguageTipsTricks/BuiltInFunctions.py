# absolute value
print(abs(-2))


# all values are true, which means either true, either not zero, either not None
print(all([1,2,3])) # true
print(all([0,1,2])) #false

# any value is true, not zero or not none
print(any([0,None,False])) # false
print(any([0,False,1])) #true

# returns ascii only representation of the object
print(ascii('something'))


# This function drops you into debugger at the call site - runs debugger console for you#
# breakpoint()  # przydaje sie jak korzystamy z wbudowanego debuggera np piszac w notatniku, w IDE sa normalne breakpointy
print('after breakpoint')

# returns a new array of bytes
print(bytearray([1,2,3]))

# returns a new byte object
print(bytes("alala", encoding="utf-8"))

# returns true if object is callable
a = lambda x: x*x
print(callable(a)) # true
print(callable("2")) # false


# creates a complex number
print(complex(3)) # (3+0j)


# allows you to invoke the expression stored in string without unpacking it
expression_in_string = "2**2"
print(eval(expression_in_string))

class Jakas:
    def printer(self):
        print('dzialam')

print(eval("Jakas().printer()"))

# the same, diffrent parameters and options if you want to dig into
print(exec("Jakas().printer()"))

# set is mutable, frozenset is hashable and immutable
secik = set([1,2,3])
secik2 = {1,2,3}
frozen_secik = frozenset([1,2,3])
print(secik)
print(secik2)
print(frozen_secik) # the diffrence is that this one is immutable and hashable

# returns the list of names in the current local scope :D :D :D :D
# prints all the attributes of the object
b = 1
print(dir(b))
print(dir())
# returns dictionary representing only locals
print(locals())
# returns dictionary representing only globals
print(globals())

# checks whether the object has attribute
#print(hasattr(object, name))

# returns hash value of an object
print(hash(b))
# returns identity of an object
print(id(b))

# returns interesting info about object and opens interactive console for you
#print(help(b))

# converts number to binary string
print(bin(123123)) # 0b11110000011110011

# converts to hex number
print(hex(255)) # 0xff
print(hex(123123)) # 0x1e0f3

# returns octal representation
print(oct(1)) # 0o1

# cheks if object is type of
print(isinstance("asd", str))

# checks if object is child of
print(issubclass(int, object))


# returns char represented by integer in unicode code
print(chr(97)) # a
print(chr(8364)) # €
# przydatne do zabawy :D :D :D

# returns unicode code of chr given
print(ord('a')) # 97
print(ord('€')) # 8364

# returns reverser iterator
lista2 = [1,2,3]
print(list(reversed(lista2))) # [3,2,1]
print(lista2[::-1]) # [3,2,1]

# rounds the value
print(round(1.23, 1)) # 1.2
print(round(1.23)) # 1
print(round(1.51)) # 2

# super()
# you can use that to invoke methods from parent class
class A:
    def elo(self):
        print('asd')

class B(A):
    def elo2(self):
        super().elo()

obj = B()
obj.elo2()

# # iterator
lista = [1,2,3,4]
iteratorek = iter(lista)
