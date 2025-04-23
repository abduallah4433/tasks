phonebook = {
'Amal':	1111111111,
'Mohammed':	2222222222,
'Khadijah':	3333333333,
'Abdullah':	4444444444,
'Rawan':	5555555555,
'Faisal':	6666666666,
'Layla':	7777777777

}

entry = input("enter number to search for the owener  of the number ")

for name,phone in phonebook.items():
    if len(entry) <10:
        print("This is invalid number")
        break
    elif   entry.isnumeric() == False:
        print('This is invalid number $')
        break
    elif phone == int(entry):
        print(name)
        break
        