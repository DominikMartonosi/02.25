szám = int(input("Adj meg egy páros számot: "))

for i in range(szám):
    if i < szám/2:
        print('O '*(i+1))
    else:
        print('O '*(szám-i))