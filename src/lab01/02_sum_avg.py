a = input()
b = input()
a = a.replace(",", ".")
b = b.replace(",", ".")
a = float(a)
b = float(b)
summ = a + b
sr_arifm = summ / 2
sr_arifm *= 100
sr_arifm = int(sr_arifm)
sr_arifm /= 100
summ *= 100
summ = int(summ)
summ /= 100
print(f"sum = {summ}; avg = {sr_arifm}")