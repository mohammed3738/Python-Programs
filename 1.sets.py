myset= {'mohammed', 1234, 2345.56,'ibrahim', True, False}
print(myset)
myset.add("baig")
print(myset)
myset.update('faraz tai')
print(myset)
myset.remove('ibrahim')
print(myset)
myset.discard("shastri")
print(myset)
myset.discard(1234)
print(len(myset))
myset.pop()
print(myset)

for items in myset:
    print('items in set are', items)
print(type(myset))
print(1234 in myset)
print('mohammed' in myset )
print("faraz tai " not in myset)

