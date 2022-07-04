age= [2, 13, 17, 20, 43]
def Myfunc(x):
    if x < 18:
        return False
    else:
        return True
father = list(filter(Myfunc,age))

for x in father:
     print(x)
