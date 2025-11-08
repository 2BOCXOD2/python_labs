# **Лабораторная работа №5**
## **Задание A**
### Код задания А
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6") # Парсер с описанием программы (выводится при --help)
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды") # Создаём подпарсеры
    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла") # Добавили подпарсер cat
    cat_parser.add_argument("--input", required=True, help="Ввести ссылу на csv файл") # Добавили аргумент --input
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки") # Добавили аргумент -n
    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов") # Добавили подпарсер stats
    stats_parser.add_argument("--input", required=True, help="Ввести ссылу на txt файл") # Добавили аргумент --input
    stats_parser.add_argument("--top", type=int, default=5, help="Задать топ") # Добавили аргумент -top
    
    args = parser.parse_args() # Получаем атрибуты из командной строки и записываем в переменную "args"

    if args.command == "cat": # Если пользователь ввёл "cat"
        csv_path = args.input # Получаем введённую ссылку
        from pathlib import Path
        import csv
        if Path(csv_path).exists(): # Проверка существования пути
            if csv_path[-4:] == ".csv": # Проверка формата файлов
                f = open(csv_path, "r", encoding="utf-8")
                st = f.read()
                f.close()
                if len(st) == 0:
                    raise ValueError # Ошибка, если файл пустой
                else:
                    with open(csv_path, "r", encoding="utf-8") as fc: # Открываем файл csv в режиме чтения
                        reader = csv.DictReader(fc) # Записываем чтение в переменную
                        coun = 1
                        if args.n == True: # Если пользователь указал нумеровать строки
                            for row in reader:
                                print(f"{coun} {row}")
                                coun += 1
                        else: # Если не нумируем строки
                            for row in reader:
                                print(row)
            else:
                raise ValueError # Ошибка, если указан не верный тип файла
        else:
            raise FileNotFoundError # Ошибка, если файл не найден
        
    elif args.command == "stats": # Если пользователь ввёл "stats"
        txt_path = args.input # Получаем введённую ссылку
        from pathlib import Path
        import sys
        import os
        sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
        import text # normalize, tokenize, count_freq, top_n
        if Path(txt_path).exists(): # Проверка существования пути
            if txt_path[-4:] == ".txt": # Проверка формата файлов
                f = open(txt_path, "r", encoding="utf-8")
                st = f.read()
                f.close()
                if len(st) == 0:
                    raise ValueError # Ошибка, если файл пустой
                else:
                    with open(txt_path, "r", encoding="utf-8") as ft: # Открываем файл txt в режиме чтения
                        st = ft.read()
                        st = str(st)
                        print(st)
                        top_n = args.top # Считываем значение "top"
                        c = text.normalize(st, casefold=True, yo2e=True) # Форматируем текст
                        c = text.tokenize(c) # Убираем лишние символы
                        c = text.count_freq(c) # Формируем словарь
                        c = text.top_n(c, top_n) # Формируем Топ
                        for x, y in c: # Выводим Топ
                            print(f"{x}: {y}")
            else:
                raise ValueError # Ошибка, если указан не верный тип файла
        else:
            raise FileNotFoundError # Ошибка, если файл не найден

b = main() # Вызываем функцию, чтобы всё работало


# python src/lab06/cli_text.py --help
# python src/lab06/cli_text.py cat --help
# python src/lab06/cli_text.py cat --input ././data/samples/people1.csv -n
# python src/lab06/cli_text.py stats --input ././data/samples/people.txt --top 3
```
### Скриншот задания №1
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/1.1.PNG)
### Скриншот задания №2
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/1.2.PNG)
### Скриншот выполнения команды --help задания А
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/1.3.PNG)
## **Задание Б**
### Код задания Б
```python
import argparse
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '../lab05'))
import json_csv
import csv_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help="Преобразовать .json в .csv")
    p1.add_argument("--input", dest="input", required=True, help="Ссылка на json")
    p1.add_argument("--output", dest="output", required=True, help="Ссылка на csv")

    p2 = sub.add_parser("csv2json", help="Преобразовать .csv в .json")
    p2.add_argument("--input", dest="input", required=True, help="Ссылка на csv")
    p2.add_argument("--output", dest="output", required=True, help="Ссылка на json")

    p3 = sub.add_parser("csv2xlsx", help="Преобразовать .csv в .xlsx")
    p3.add_argument("--input", dest="input", required=True, help="Ссылка на csv")
    p3.add_argument("--output", dest="output", required=True, help="Ссылка на xlsx")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json_path = args.input # Считали ссылку на читаемый файл
        csv_path = args.output # Считали ссылку для записываемого файла
        otvet = json_csv.json_to_csv(json_path, csv_path) # Загружаем ссылки в функцию и выполняем её

    elif args.cmd == "csv2json":
        csv_path = args.input # Считали ссылку для записываемого файла
        json_path = args.output # Считали ссылку на читаемый файл
        otvet = json_csv.csv_to_json(csv_path, json_path) # Загружаем ссылки в функцию и выполняем её

    elif args.cmd == "csv2xlsx":
        csv_path = args.input # Считали ссылку для записываемого файла
        xlsx_path = args.output # Считали ссылку на читаемый файл
        otvet = csv_xlsx.csv_to_xlsx(csv_path, xlsx_path) # Загружаем ссылки в функцию и выполняем её

d = main()

# python src/lab06/cli_convert.py json2csv --input ././data/samples/people.json --output ././data/out/06json2csv.csv
# python src/lab06/cli_convert.py csv2json --input ././data/samples/people1.csv --output ././data/out/06csv2json.json
# python src/lab06/cli_convert.py csv2xlsx --input ././data/samples/people1.csv --output ././data/out/06csv2xlsx.xlsx
```
### Скриншот выполнения команды --help задания Б
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/2.1.PNG)
### Скриншот записанного файла "json2csv"
![05](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/2.2.PNG)
### Скриншот записанного файла "csv2json"
![06](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/2.3.PNG)
### Скриншот записанного файла "csv2xlsx"
![07](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab06/2.4.PNG)