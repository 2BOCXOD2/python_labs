def min_max(spisok):
    minn = float("inf")
    maxx = -float("inf")
    for i in spisok:
        minn = min(minn, i)
        maxx = max(maxx, i)
    return (minn, maxx)


spisok_1 = [1, 2, -3, 5.6]
otvet_1 = min_max(spisok_1)

print(otvet_1)