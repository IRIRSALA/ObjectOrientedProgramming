#Decoration and Wrapping function 


def hello():
    return "Hello World"

def mydeco(func):
    def Wrapper():
        greeting = "Wrapper says"
        return f"{greeting} {func()} !!!"
    return Wrapper
myhello = mydeco(hello)
print(myhello())

def add(*args,**kwargs):
    result = 0
    for x in args:
        result += x
    for y,z in kwargs.items():
        result += z
    return result

kwargs = {"arg1":20,"arg2":30}
args = [20,30,80]
def mydeco_add(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return f'my decorated result: {result}'
    return wrapper


my_add = mydeco_add(add)
print(my_add(*args,**kwargs))
@mydeco_add
def add(*args):
    '''Sum any numbers together, the long way'''
    total = 0
    for item in args:
        total +=item
    return total
print(add(20,30,10))
@mydeco_add
def add(a,b):
    '''return adding'''
    return a+b
print(add(10,20))

from functools import wraps
def mydeco_add_b(func):
    @wraps(func)
    def wrapper2(*args,**kwargs):
        #result = func(*args,**kwargs)
        return f'{func(*args,**kwargs)}!!!'
    return wrapper2

@mydeco_add_b
def add_b(*args):
    '''Sum any numbers together, the long way'''
    total = 0
    for item in args:
        total +=item
    return total

print(add_b(2,4,6,-6))