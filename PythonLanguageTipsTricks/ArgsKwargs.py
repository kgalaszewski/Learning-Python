# Args are used to pass more than 1 params to the method without specyfing specifications in method signature
def method_requiering_args(sth, sth2, *args):
    print(args[0]) # we can do it but we can't be sure how many args will be passed
    print(args[1])
    print (args) # will return args as a tuple

method_requiering_args('lelo', 'lelo2', 'lelo3', 'lelo4', 'lelo5', 'lelo6') # ('lelo3', 'lelo4', 'lelo5', 'lelo6')


# Kwargs are used to pass more than 1 Key Word params to the method without specyfing specifications in method signature
def method_requiering_kwargs(sth, sth2, **kwargs):
    print(kwargs['next_one']) # we can do it but we have to ensure somehow that key named next_onewill exist
    print(kwargs) # will return dictionary {'next_one': 3, 'next_one2': 4, 'next_one3': 5}

method_requiering_kwargs(1, 2, next_one=3, next_one2=4, next_one3=5)
method_requiering_kwargs(1, 2, 3) # will throw error, only 2 positional arguments (sth, sth2). Third one and all others have to be key word args


# combining regular args, *args and **kwargs
def method_give_me_what_you_want(something, *args, **kwargs):
    print(something) # will return 'abc'
    print(args) # will return ('dde','eee')
    print(kwargs) # will return {'sth':1, 'sth2':2, 'sth3': 3}

method_give_me_what_you_want('abc', 'dde', 'eee', sth=1, sth2=2, sth3=3)


# passing dict to method accepting kwargs as kwargs
def method_using_kwargs(**kwargs):
    print(kwargs)

values = {
    'Name': 'Kodi',
    'Age': 5,
    'Breed': 'Border Collie',
    'Color': 'Black-White'
}

method_using_kwargs(**values) # without stars here, it would take dict as one arg

method_using_kwargs(**{
    'name': 'Markiz',
    'breed': 'Sheltie'
})

# passing tuple / list to method accepting args
def method_using_args(*args):
    print(args)

vals = [1, 2, 3, 4]
vals2 = (3, 3, 4, 4)
method_using_args(*vals) # without star here, it would take list as one arg
method_using_args(*vals2) # without star here, it would take tuple as one arg

method_using_args(*[5, 5, 5])


# combining all of the above
def method_accepting_everything(norm_arg, *args, **kwargs):
    print(norm_arg)
    print(args)
    print(kwargs)

val = 'Kodi'
vals = (1, 2, 3)
vals2 = {'Name': 'Kodi', 'Age': 5}

method_accepting_everything(val, *vals, **vals2)

method_accepting_everything('siemanko', *[4, 4], **{
    'sth': 1,
    'sth2': 2
})


# Specifying exact number of *args but in practise they have to be kwargs
def kargs_method_advanced(sth, sth2, *, name, age):
    print(f'{sth} {sth2} {name} {age}')

kargs_method_advanced(1, 2, name='Kodi', age=5)
kargs_method_advanced(1, 2, 'Kodi', 5) # will throw an TypeError because Kodi and 5 are not keyword args and they have to be 
