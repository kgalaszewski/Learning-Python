import time

lista = [1,2,3,4,5,6,7,8,9,10]

def get_list() -> list:
    for element in lista:
        print('zwracam 1 element')
        yield element

def process_list_by_single_element():
    slista = get_list()

    for single_element in slista:
        print(single_element)
        time.sleep(.5)


process_list_by_single_element()

