def unique_sorted(spisok):
    unique_spisok = []
    for i in spisok:
        if i in unique_spisok:
            pass
        else:
            unique_spisok.append(i)
    unique_spisok.sort()
    return unique_spisok

# spisok_2 = [3, 3, 4, 2, 1, 1, 2, 5, -1.2, -3.6, -1.2]
# otvet_2 = unique_sorted(spisok_2)
# print(otvet_2)