from functools import reduce

val = [1,2,3,4,5]
max= reduce(lambda a,b:a if a>b else b, val)
print("max value =", max)