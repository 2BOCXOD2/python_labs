from pathlib import Path
def read_text(path: str, encoding: str = "utf-8"):
    if type(path) == str:
        if encoding == "utf-8": # Проверяем кодировку
            if Path(path).exists(): # Проверяем наличие файла по заданному пути
                f = open(path, "r") # Считываем файл
                st = f.read() # Записываем весь файл в строку
                f.close() # Закрываем файл
                return st # Возвращаем строку
            else:
                raise FileNotFoundError # Файл позаданному пути не существует
        else:
            raise UnicodeDecodeError # Можно выбрать другую кодировку при сохранении файла в блокноте
    else:
        raise ValueError

# print(read_text("././data/lab04/input.txt", "utf-8"))


def write_csv(rows, path, header=None): # Передаём в функцию данные, путь для сохранения решения, заголовок
    import csv
    from pathlib import Path
    if (not rows): # Если данные не переданы
        if header == None: # Проверяем, пустой ли заголовок
            f = open(path, "w", newline="", encoding="utf-8") # Если пустой - создаём пустой файл
        else:
            f = open(path, "w", newline="", encoding="utf-8") # Иначе создаём файл и записываем header
            csw_zapis = csv.writer(f)
            csw_zapis.writerow(header)
            f.close() # Закрываем файл
    else:
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            for j in range(len(rows) - 1): # Проверяем длину каждого элемента данных
                if len(rows[j]) != len(rows[j+1]):
                    raise ValueError
            w = csv.writer(f) # Создаём удобную переменную записи
            if header is not None: # Проверяем наличие заголовка и записываем его
                w.writerow(header)
            for r in rows: # Записываем данные в файл
                w.writerow(r)
b = write_csv([(1, 2), (3, 4)], "././data/lab04/check.csv", ("a", "b"))

        # f = open(path, "w", newline="", encoding="utf-8")
        # csw_zapis = csv.writer(f)
        # csw_zapis.writerow(header)
        # csw_zapis.writerows(rows)

# f = open("C:/Users/GN/Desktop/python_labs/data/lab04/input.txt", "r")
# f = open("././data/lab04/input.txt", "r")
# res = f.read()
# print(res)
# f.close()
