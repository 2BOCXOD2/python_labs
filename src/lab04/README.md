# **Лабораторная работа №4**
## **Задание A**
### Код задания №1
```python
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
        raise ValueErrorfrom pathlib import Path

# print(read_text("././data/lab04/input.txt", "utf-8"))
```
### Скриншот задания №1
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab04/1.1.PNG)
### Код задания №2
```python
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
# b = write_csv([(1, 2), (3, 4)], "././data/lab04/check.csv", ("a", "b"))
```
### Скриншот задания №2
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab04/1.2.1.PNG)
### Скриншот записанного файла
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab04/1.2.2.PNG)
## **Задание B**
### Код задания B
```python
import sys
import os
from pathlib import Path
sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
from io_txt_csv import write_csv
import text # normalize, tokenize, count_freq, top_n
path_in = "././data/lab04/input.txt"
# path_x = input() #
path_a = "././data/lab04/a.txt"
path_b = "././data/lab04/b.txt"
if Path(path_in).exists(): # Проверяем наличие входного файла

    with open(path_in, mode="r", newline='', encoding='utf-8') as f:
        st = f.read()
        top = 5
        a = text.normalize(st, casefold=True, yo2e=True) # Форматируем текст
        a = text.tokenize(a) # Убираем лишние символы
        a = text.count_freq(a) # Формируем словарь
        a = text.top_n(a, 5) # Формируем Топ
        z = []
        for item in a:
            z.append(item)
        write_csv(z, "././data/lab04/report.csv", ("Слово", "Частота"))
        print(f"Всего слов: {len(st.split())}")
        print(f"Уникальных слов: {len(a)}")
        print('Топ-5:')
        #for x, y in a: # Выводим Топ
        #    print(f"{x}: {y}")
        print("______________________") # Выводим данные красиво
        max_len = 5 # Минимальная ширина столбца "Слово"
        for r, t in a: # Поиск максимальной длины слова
            max_len = max(max_len, len(r))
        print(f"Слово{" " * (max_len - 4)}| Частота") # Красиво выводим слово и частоту ровными столбцами
        print("----------------------")
        for x, y in a: # Выводим Топ красиво
            print(f"{x}{" " * (max_len - len(x) + 1)}| {y}") #Красиво выводим слово и частоту ровными столбцами
else:
    raise FileNotFoundError # Если файла нет - ошибка
```
### Скриншот задания B
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab04/3.1.PNG)
### Скриншот записанного файла
![05](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab04/2.4.PNG)