def format_record(rec: tuple[str, str, float]):
    for i in rec:
        if i == '':
            raise ValueError
    new_dannye = ""
    fio = rec[0]
    fio = fio.split()
    new_fio = str(f"{str.capitalize(fio[0])} ")
    for a in fio[1:3]:
        new_fio = new_fio + str.capitalize(a[0]) + '.'
    new_dannye += f"{new_fio}, "
    new_dannye += f"{rec[1]}, "
    gpa = rec[2]
    gpa = round(gpa, 2)
    gpa = str(gpa)
    if len(gpa) == 1:
        gpa = gpa + ".00"
    elif len(gpa) == 3:
        gpa = gpa + "0"
    new_dannye += f"{gpa}"

    return new_dannye

# dannye = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
# otvet = format_record(dannye)
# print(otvet)