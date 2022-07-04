val = [6, 12, 17, 19, 20, 14]
def Myfunc(x):
    if x%2==0:
        return True
    else:
        return False
calling = list(filter(Myfunc, val))
for x in calling:
    print(x)