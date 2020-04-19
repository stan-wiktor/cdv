slownik = {'key1':'value1', 'key2':'value2'}

pracownik = {
    'imie':'Jan', 
    'nazwisko':'Kowalski', 
    'miasto':'Poznań', 
    'wiek':'38', 
    'imionaDzieci':['Pawel', 'Alicja'], 
    'imionaRodzicow':['Adam', 'Marta']
}
print(pracownik)
print(pracownik['imionaDzieci'][0])

pracownik['wzrost']=175
pracownik['waga']=80
print(pracownik)

pracownik1 = {
    'name':'Anna',
    'surname':'Kowalska',
    'city':'Poznań',
    'age': 24
}
print()
print(pracownik1)

key = 'age'
if key in pracownik1:
    del pracownik1[key]
    print(f'Klucz {key} zostal usuniety')
else:
    print(f'Klucz {key} nie zostal usuniety')

print(pracownik1)
print(pracownik1.keys())
print(pracownik1.values())

print(list(pracownik1.values()))
print(pracownik1.items())

for value in pracownik1.values():
    print(value, end=" ")

print()
for key, value in pracownik1.items():
    print(f'{key}: {value}')

