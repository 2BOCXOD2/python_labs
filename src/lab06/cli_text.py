import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")
    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    # подкоманда stats
    # stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    # stats_parser.add_argument("--input", required=True)
    # stats_parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()
    if args.command == "cat":
        csv_path = args.input
        print(csv_path)
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
                        if args.n == True:
                            for row in reader: # Для каждого словаря
                                print(f"{coun} {row}")
                                coun += 1
                        else:
                            for row in reader: # Для каждого словаря
                                print(row)
            else:
                raise ValueError # Ошибка, если указан не верный тип файла
        else:
            raise FileNotFoundError # Ошибка, если файл не найден
    elif args.command == "stats":
        """ Реализация команды stats """

a = main()

# python Desktop/python_labs/src/lab06/cli_text.py cat --input Desktop/python_labs/data/samples/people1.csv



# import argparse

# parser = argparse.ArgumentParser(description="Простая программа приветствия")  
# parser.add_argument("--name", required=True, help="Имя пользователя")
# args = parser.parse_args()  
# print(f"Привет, {args.name}!")  
# python src/lab06/cli_text.py --name Ali # В визал студио
# python Desktop/python_labs/src/lab06/cli_text.py --name Ali # В терминале виндоус