def flatten(spisok):
    new_spisok = []
    for i in spisok:
        if isinstance(i, (list, tuple)):
            for j in i:
                new_spisok.append(j)
        else:
            return TypeError
    return new_spisok

# spisok_3 = [[1, 2], "ab"]
# otvet_3 = flatten(spisok_3)
# print(otvet_3)