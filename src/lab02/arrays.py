"""
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
"""
'''
def unique_sorted(spisok):
    unique_spisok = []
    for i in spisok:
        if i in unique_spisok:
            pass
        else:
            unique_spisok.append(i)
    unique_spisok.sort()
    return unique_spisok

spisok_2 = [3, 3, 4, 2, 1, 1, 2, 5, -1.2, -3.6, -1.2]
otvet_2 = unique_sorted(spisok_2)
print(otvet_2)
'''

def flatten(spisok):
    