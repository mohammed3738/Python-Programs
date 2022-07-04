age = [12, 14, 15, 17, 18, 22, 27]

def func(x):
    if x < 18:
        return False
    else:
        return True
def func1(x):
    return x * x

adults= list(filter(func, age))

for x in adults:
    print(x)

square= list(map(func1, adults))
for x in square:
    print(x)