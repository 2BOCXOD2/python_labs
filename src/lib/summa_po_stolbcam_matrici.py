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

# matrica_3 = [[1, 2, 3], [4, 5, 6]]
# otvet_3 = col_sums(matrica_3)
# print(otvet_3)