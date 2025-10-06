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

# matrica_2 = [[-1, 1], [10, -10]]
# otvet_2 = row_sums(matrica_2)
# print(otvet_2)