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


# # properties like in C#
# class TestowaKlasa:
#     def __init__(self):
#         self.__zmienna1 = 1

#     @property
#     def zmienna1(self):    # property musi miec inna nazwe niz zmienna bo inaczej rekurencja
#         return self.__zmienna1

# obj = TestowaKlasa()
# print(obj.zmienna1)


# # Docstring - komentarzowa dokumentacja
# def moja_funkcja(nazwa: str, wiek: int) -> bool:
#     """ moja_funkcja(nazwa: str, wiek: int) -> zwraca true jesli elo benc # NIE PISZ TEJ LINIJKI JAK NIC NIE ZWRACA ELO BENC

#         Parameters :
#         nazwa: str => musi byc taka siaka i owaka
#         wiek: int => musi byc taki siaki i owaki

#         Raises :
#         ElobencError gdy sie zdenerwuje
#     """
#     return True if True else False

# moja_funkcja('asd', 123) # WSZYSTKO LADNIE DOKUMENTUJE JAK W C#, ze widac w IDE jak cos wywolujesz



# # KeyWord only arguments
# def funkcja(a: str, b, c=True) # TUTAJ zadnego parametru nazwy nie musisz podac
#     pass

# def funkcja_uzywajaca_keyword_arguments(a, b: str, *, c = True) # Tutaj wszystkie na prawo od gwiazdki musisz podac nazwe np. c
#     pass

# # Yield lazy loading example 
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def get_list() -> list:
#     for element in lista:
#         print('zwracam 1 element')
#         yield element

# def process_list_by_single_element():
#     slista = get_list()

#     for single_element in slista:
#         print(single_element)
#         time.sleep(.5)

# process_list_by_single_element()


# # klasy tips
# class Testowa:
#     maciek = 'maciek'

# class Testowa2:
#     def __init__(self):
#         self.maciek = 'maciek'

# t1 = Testowa()
# t2 = Testowa2()
# setattr(t1, 'new_field', 'its_value')
# setattr(t2, 'new_field', 'its_value')
# print(t1.new_field)
# print(t2.new_field)
# print(getattr(t1, 'new_field')) # to to samo robi co 2 linijki wyzej tylko ladniej 




