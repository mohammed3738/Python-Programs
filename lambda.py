# Example program without using lambda Keyword
def add(a,b):
    c = a + b
    return c
print("The addition of 2 and 7 is",add(2,7))

def substract(d,e):
    f = d - e
    return f
print('The substraction of 2 and 7 is',substract(2,7))

def mul(g,h):
    return g*h
print("The multiplication of 2 and 7 is",mul(2,7))

def div(i,j):
    return i/j
print("The division of 2 and 7 is",div(2,7))

#Example using lamba Keyword



addition=lambda x,y:x+y
print("The addition of 2 and 7 is",addition(2,7))

substraction=lambda a,b:a-b
print("The substraction of 2 and 7 is",substraction(2,7))

multiplication=lambda c,d:c*d
print('The multiplication of 2 and 7 is',multiplication(2,7))

division=lambda e,f:e/f
print("The dividion of 2 and 7 is",division(2,7))
