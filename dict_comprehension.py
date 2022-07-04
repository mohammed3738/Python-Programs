squareofnumbers={number:number**2 for number in range(11) if number%2==0}
print(squareofnumbers)
print(type(squareofnumbers))

oddnumbers={number:number**2 for number in range (11) if number&2!=0}
print(oddnumbers)