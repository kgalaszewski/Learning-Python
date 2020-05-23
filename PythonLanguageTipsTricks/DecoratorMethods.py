# Decorator methods are often used to wrap some other method to measure the execution time or add additional logging
def decorator_method(func):
    def my_wrapper(number):
        print('started decorator method')
        func(number)
        print('finished decorator method')
    return my_wrapper

@decorator_method
def normal_method(number: int):
    print(number)

normal_method(2)


# Generic decorator method using *args and **kwargs
def generic_decorator_method(my_func):
    def generic_wrapper(*args, **kwargs):
        print('started decorator method')
        my_func(*args, **kwargs)
        print('finished decorator method')
    return generic_wrapper

@generic_decorator_method
def normal_method2(number: int):
    print(number)

@generic_decorator_method
def diffrent_method(name, age, *, breed, color):
    print(name + str(age) + breed + color)

@generic_decorator_method
def yet_another_diffrent_method():
    print("I don't need args")

@generic_decorator_method
def yet_another2(is_true: bool=True, **kwargs):
    print(is_true)
    print(kwargs)

diffrent_method('Kodi', 5, breed='BorderCollie', color='black-white')
yet_another_diffrent_method()
yet_another2(False, sth=1, sth_else='else')