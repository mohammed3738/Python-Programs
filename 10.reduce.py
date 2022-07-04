from functools import reduce
val = [1,2,3,4,5]

def myfunc(a,b):
    if a > b:
        return a
    else:
        return b
max = reduce(myfunc, val)
print("Max number = ",max)