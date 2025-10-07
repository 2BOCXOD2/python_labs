'''
def transpose(matrica):
    if matrica == []:
        return []
    else:
        stroki = len(matrica[0])
        stolbci = len(matrica)
        new_matrica = []
        for i in matrica:
            if stroki != len(i):
                return ValueError
        for x in range(stroki):
            spi = []
            for y in range(stolbci):
                spi.append(matrica[y][x])
            new_matrica.append(spi)
        return new_matrica
matrica_1 = [[1, 2], [3, 4]]
otvet_1 = transpose(matrica_1)
print(otvet_1)     
'''
"""
def row_sums(matrica):
    new_matrica = []
    stolbci = len(matrica)
    stroki = len(matrica[0])
    for i in matrica:
        if stroki != len(i):
            return ValueError
    for x in range(stolbci):
        summ = 0
        for y in range(stroki):
            summ += matrica[x][y]
        new_matrica.append([summ])
    return new_matrica

matrica_2 = [[-1, 1], [10, -10]]
otvet_2 = row_sums(matrica_2)
print(otvet_2)
"""

def col_sums(matrica):
    new_matrica = []
    stolbci = len(matrica)
    stroki = len(matrica[0])
    for i in matrica:
        if stroki != len(i):
            return ValueError
    for x in range(stroki):
        summ = 0
        for y in range(stolbci):
            summ += matrica[y][x]
        new_matrica.append([summ])
    return new_matrica

matrica_3 = [[1, 2, 3], [4, 5, 6]]
otvet_3 = col_sums(matrica_3)
print(otvet_3)