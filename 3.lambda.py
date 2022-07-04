from argparse import ArgumentDefaultsHelpFormatter


age = [12, 13, 16, 18, 24, 29]
adults= filter(lambda a: a > 18, age)
for x in adults:
    print(x)