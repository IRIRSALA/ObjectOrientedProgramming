from functools import wraps

#def add(x,y):
 #   return x + y
#print(add(5,6))

def add(*args,**kwargs):
    result = 0
    for x in args:
        result += x
    for y,z in kwargs.items():
        result += z
    return result
kwargs = {"arg1":20,"arg2":30}
args = [20,30,80]
print(add(20,30,80,**kwargs))
print(add(*args,**kwargs))