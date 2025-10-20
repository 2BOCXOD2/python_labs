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

print(read_text("././data/lab04/input.txt", "utf-8"))



# f = open("C:/Users/GN/Desktop/python_labs/data/lab04/input.txt", "r")
# f = open("././data/lab04/input.txt", "r")
# res = f.read()
# print(res)
# f.close()