mydict = {'first_name': 'babu','last_name':'ramakrishna', 'gender':'male', 'age':'21', 'place':'banglore'}
print(mydict)
print(len(mydict))
for items in mydict:
    print("The Key name and Value pair in Dictonary are :",mydict [items])
print(type(mydict))
firstname= mydict['first_name']
lastname= mydict['last_name']
Gender=mydict['gender']
Age= mydict['age']
Place=mydict['place']
print('The first name is :', firstname)
print("The last name is :", lastname)
print("The gender is :", Gender)
print("The age is :", Age ) 
print("The place is :", Place ) 
print(mydict.get('age'))
print(mydict.get('place'))
print(mydict.get('babu'))
print(mydict.get('firstname'))
print(mydict.get('first_name'))
mydict['hobby']='playing chess'
print(mydict)
mydict.pop('age')
print(mydict)
del mydict['hobby']
print(mydict)