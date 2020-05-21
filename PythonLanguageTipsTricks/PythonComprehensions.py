# Dict comprehensions
lista = [1,2,3,4,5]
new_dict = {a: (2*a) for a in lista}
print(new_dict)

some_dict = {1: 'a', 2: 'b'}
some_dict2 = {11: 'aa', 22: 'bb'}
new_dict = {ki:walju for para in (some_dict, some_dict2) for ki, walju in para.items()}
print(new_dict)


# Tworzenie set'a
secik = set([1, 2, 3, 4, 5])
rowniez_secik = {1, 2, 3, 4, 5} # Jak nie podajesz key value to z tymi nawiasami nie dict tylko set
print(secik)
print(rowniez_secik)


# check for empty string
test = ' '
print(test == ' ')
print(test.isspace()) # to dokladnie to samo ale ladniej

# inne metody na strincach - jest jeszcze wiecej niz wypisane nizej 
print(test.isalnum())
print(test.isalpha())
print(test.isdigit())
print(test.isascii())
print(test.isprintable())
print(test.isnumeric())