MyTuple = (1,'mohammed',234.44,'baig',66j,True,False)
print(MyTuple)
print(type(MyTuple))
print(len(MyTuple))
print(MyTuple[0])
print(MyTuple[-4])
print(MyTuple[-5])
print(MyTuple[2:6])
print('albin' in MyTuple)
print('mohammed' in MyTuple)
print('mohammed'not in MyTuple)

for items in MyTuple:
    print("one by one print items in the tuple", items)
