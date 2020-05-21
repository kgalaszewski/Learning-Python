# name = [22, 33, 123]

# for index, value in enumerate(name):
#     print(f'index of {value} is equal to {index}')

# first_collection = [1, 2, 3, 4, 5]
# second_collection = ['I', 'II', 'III', 'IV', 'V']
# third_collection = ['a', 'b', 'c', 'd', 'e']

# for first, second, third in zip(first_collection, second_collection, third_collection): # tak naprawde 3 llisty leca jak jedna lista tupli
#     print(f'{first} == {second} == {third}')

# # loop through dict 
# my_dict = {'a': 1, 'b': 2}

# for key, value in my_dict.items(): # items to tak naprawde keyValuePair
#     print(f'klucz to {key}, value = {value}')

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# #
# # ENUMERATE pomaga, jak chcemy iterowac po liscie z customowym indexem

# # Zip pomaga jak chcemy loopowac po wielu kolekcjach jednoczesnie, cos jakby to byl tuple 

# # Pythonskie linq
# lis = [1,2,3,4,5] 
# list3 = list(filter(lambda x: x > 3, lis))

# # Pythonskie linq 2
# listeczka = [1, 2, 3, 4]
# lisa = list(map(lambda x: x**3, listeczka))


# # itertools
# vals = [1,2,3,4,5,4,3]
# acc = itertools.accumulate(vals) # it translates the list to list of  [(value + previous value), (value + previous value), (value + previous value)] :D :D
# acc2 = itertools.accumulate(vals, max) # it will iterate all the values normally till it gets to the max value, it keeps repeating max till the end
# itertools.chain("ANCD", "1234") # will combine chars from string and numbers to list [a, n, c, d, 1, 2, 3, 4]
# # to wyzej to cos jak append w deque ??

# # LINQ CIAG DALSZY
# itertools.dropwhile(lambda x: x is None, vals) # wywali wszystkie dla ktorych lambda zwroci false a potem wezmie wszystkie
# itertools.takewhile(lambda x: x is None, vals) # wezmie wszystkie do momentu az pierwszy false, wtedy przestanie brac cokolwiek


# # Cycle() w pythonie to infinite operator, czyli pętla ktora nie konczy sie po pierwszym przeiterowaniu wszystkiego po razie 

# # collections
# Point = collections.namedtuple("Point", "x y z") # Point will be the name and 3 arguments will be created as a tuple
# p1 = Point(1, 3, 5)
# print(p1.y, p1.z) # czyli jak potrzebujemy klase ktora ma miec tylko kilka zmiennych to lepiej zrobic named tuple, tuple sa szybciutkie i leciutkie


# # Counter
# from collections import Counter

# listeczka = [1, 2, 2, 2, 3, 4, 4, 5]
# counter_listeczki = Counter(listeczka)
# counter_listeczki = counter_listeczki[2]  # zwroci 3 bo tyle razy wystepuje 2
# najczesciej_powtarzajacy_sie = counter_listeczki.most_common(2) # zwroci 2 najczesciej powtarzajace sie elementy w liscie i po ile razy czyli (2, 3) i (4, 2)

# lista1= [1,2,3]
# lista2 = [1,2]
# wspolne_el = lista1 & lista2


# # Istnieje OrderedDict ktory trzyma pary w kolejnosci dodania \
# from random import random
# rand = random() # wylosuje randomowa liczbe jako float reprezentujacy %, czyli np 0.72345 i trzeba za kazdym razem tworzyc obiekt random() zeby miec nowy


# # Liczby zmienno przecinkowe
# float1 = 2.22
# float2 = .123 # NIE TRZEBA DAWAC 0 przed przecinkiem
# are_bigger = float1 > .99 and float2 > .99 # NIE TRZEBA DAWAC 0 przed przecinkiem

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
