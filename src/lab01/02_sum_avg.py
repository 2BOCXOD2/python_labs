a = input()
b = input()
a = a.replace(",", ".")
b = b.replace(",", ".")
a = float(a)
b = float(b)
summ = a + b
print(f"sum = {summ:.2f}; avg = {(summ / 2):.2f}")