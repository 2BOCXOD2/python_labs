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
# matrica_1 = [[1, 2], [3, 4]] # [[1, 2, 3]]
# otvet_1 = transpose(matrica_1)
# print(otvet_1)     