fio = input()
alf = "АБВГДИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
new_fio = ""
fio1 = ""
for i in fio:
    if i in alf:
        new_fio += i
fio = fio.split()
for j in fio:
    fio1 += j
dlin = len(fio1) + 2
print("Инициалы:", new_fio)
print("Длина (символов):", dlin)