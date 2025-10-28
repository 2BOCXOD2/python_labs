def csv_to_xlsx(csv_path: str, xlsx_path: str):
    from pathlib import Path
    import csv
    import openpyxl
    if Path(csv_path).exists(): # Проверка существования пути
        if csv_path[-4:] == ".csv": # Проверка формата файлов
            f = open(csv_path, "r", encoding="utf-8")
            st = f.read()
            f.close()
            if len(st) == 0:
                raise ValueError # Ошибка, если файл пустой
            else:
                wb = openpyxl.Workbook() # Создаём новый файл
                ws = wb.active # Создаём новый лист
                ws.title = "Лист1" # Называем новый лист
                with open(csv_path, "r", encoding="utf-8") as fc: # Открываем csv файл
                    for row in csv.reader(fc): # Построчно считываем
                        ws.append(row) # Записываем построчно
                        wb.save(xlsx_path) # Сохраняем файл

a = csv_to_xlsx("././data/samples/people1.csv", "././data/out/people.xlsx")