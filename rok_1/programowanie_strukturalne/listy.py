programowanie=['Python', 'PHP', 'C#', 'JS', 'Java']
print(programowanie)
print (type(programowanie))

first=programowanie[0]
print(first)

threeElements=programowanie[0:3]
print(threeElements)

lastElement = programowanie[-1]
print(lastElement)

#dodawanie nowego elementu na koniec listy
programowanie.append('R')
programowanie.append('Python')
print(programowanie)

#zliczanie elementów w liście
countElements=programowanie.count('Python')
print(countElements)

#ilość elementów w liście
countTotalElements = len(programowanie)
print(countTotalElements)

#łączenie list
secondList = ['C', 'C++']
programowanie.extend(secondList)
print(programowanie)
print(secondList)

#czyszczenie listy
new=programowanie
print('Lista nowa: ', end="")
print(new)

new.clear()
print('Lista nowa: ', end="")
print(new)
print("Lista programowania: ", end="")
print(programowanie)
