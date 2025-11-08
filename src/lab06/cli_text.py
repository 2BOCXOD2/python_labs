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


# python Desktop/python_labs/src/lab06/cli_text.py cat --input Desktop/python_labs/data/samples/people1.csv





# import argparse

# parser = argparse.ArgumentParser(description="Простая программа приветствия")  
# parser.add_argument("--name", required=True, help="Имя пользователя")
# args = parser.parse_args()  
# print(f"Привет, {args.name}!")  
# python src/lab06/cli_text.py --name Ali # В визал студио
# python Desktop/python_labs/src/lab06/cli_text.py --name Ali # В терминале виндоус