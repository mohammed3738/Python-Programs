from unicodedata import name


nesteddict= {'dict1':
{
    'name':'babu',
    'age':'21'
},
'dict2':
{
    'name':'mohammed',
    'age':'23'

},
'dict3':
{
    'name':'ibrahim',
    'age':'23'
}

}
print(nesteddict)
print(nesteddict['dict1']['name'])
print(nesteddict['dict2']['name'])
print(nesteddict['dict3']['name'])
print(nesteddict['dict1']['age'])
