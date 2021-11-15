import functools
'''Decorator Function '''
def decorator(func):
    @functools.wraps(func)
    def inner():
        '''Using function wrapper as a variable'''
        str1=func
        return str1.upper()
    return inner


''' Making greet function as a decorator '''
@decorator
def greet():
    return "good morning"

''' Here we will get inner as output because decorator
hides certain properties of a function like docstring, parameters.
Which means it will hide data of original function'''
'''But if we uncomment line no 4 we will find that it prints greet
as @functools.wraps(func) copies the original data'''
print(greet) 
print(greet.__name__) 