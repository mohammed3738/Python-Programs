numbers = [12, 14, 15, 16, 19, 21]

even = list(filter(lambda a : a%2==0, numbers))
for x in even:
    print(x)