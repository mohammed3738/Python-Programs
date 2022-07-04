age = [12, 14, 17, 18, 22, 29]
adults= list(filter(lambda a:a > 18, age))
square= list(map(lambda a:a*a, adults))
for x in adults:
    print(x)
for x in square:
    print(x)
