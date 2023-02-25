sor = 5
oszlop = 5
lista = []

for i in range(sor):
    row = []
    for j in range(oszlop):
        if i == j:
            row.append('O')
        else:
            row.append('.')
    lista.append(row)

for row in lista:
    for cell in row:
        print(cell, end=' ')
    print()
