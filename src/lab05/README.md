# **Лабораторная работа №5**
## **Задание A**
### Код задания №1
```python
def json_to_csv(json_path: str, csv_path: str):
    from pathlib import Path
    import json
    import csv
    if Path(json_path).exists(): # Проверка существования пути
        if json_path[-5:] == ".json" and csv_path[-4:] == ".csv":
            f = open(json_path, "r", encoding="utf-8")
            st = f.read()
            f.close()
            if len(st) == 0:
                raise ValueError # Ошибка, если файл пустой
            else:
                with open(json_path, "r", encoding="utf-8") as fj:
                    data = json.load(fj)
                x = data[0].keys() # Сохраняем изначальный порядок колонок
                with open(csv_path, "w", newline='', encoding="utf-8") as fc:
                    writer = csv.DictWriter(fc, fieldnames=x, extrasaction="raise") # Переменная для удобной записи (файл для записи, порядок колонок, вывод ошибки если ключ не найден)
                    writer.writeheader()
                    writer.writerows(data)
        else:
            raise ValueError # Ошибка, если указан не верный тип файла
    else:
        raise FileNotFoundError # Ошибка, если файл не найден
# a = json_to_csv("././data/samples/people.json", "././data/out/people.csv")
```
### Скриншот задания №1
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.1.PNG)
### Скриншот записанного файла
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.2.PNG)
### Код задания №2
```python
def csv_to_json(csv_path: str, json_path: str):
    from pathlib import Path
    import json
    import csv
    if Path(csv_path).exists(): # Проверка существования пути
        if json_path[-5:] == ".json" and csv_path[-4:] == ".csv": # Проверка формата файлов
            f = open(csv_path, "r", encoding="utf-8")
            st = f.read()
            f.close()
            if len(st) == 0:
                raise ValueError # Ошибка, если файл пустой
            else:
                with open(csv_path, "r", encoding="utf-8") as fc: # Открываем файл csv в режиме чтения
                    reader = csv.DictReader(fc) # Записываем чтение в переменную
                    data = [] # Создаём переменную для хранения словарей
                    for row in reader: # Для каждого словаря
                        data.append(row) # записываем его в список
                with open(json_path, "w", newline='', encoding="utf-8") as fj: # Открываем json файл
                    json.dump(data, fj, ensure_ascii=False, indent=2) # Записываем в него список словарей, выводя только ASCII символы, отступ уровня важности равен 2
        else:
            raise ValueError # Ошибка, если указан не верный тип файла
    else:
        raise FileNotFoundError # Ошибка, если файл не найден
# a = csv_to_json("././data/samples/people1.csv", "././data/out/people1.json")
```
### Скриншот задания №2
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.3.PNG)
### Скриншот записанного файла
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.4.PNG)
## **Задание B**
### Код задания B
```python
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
```
### Скриншот задания B
![05](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.5.PNG)
### Скриншот записанного файла
![06](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab05/1.6.PNG)