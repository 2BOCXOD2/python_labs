# **Лабораторная работа №7**
## **Создание и заполнение pyproject.toml**
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/0.PNG)
## **Задание A**
### Код задания A
```python
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Добавили путь в папку с функциями
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт \nМИр \t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello \r \nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source, casefold=True, yo2e=True) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("hello,world!!!", ["hello", "world"]),
        ("это по-настоящему круто", ["это", "по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        (["a","b","a","c","b","a"], {"a":3,"b":2,"c":1}),
        (["bb","aa","bb","aa","cc"], {"aa":2,"bb":2,"cc":1}),
    ],
)
def test_count_freq_and_top_n(source, expected):
    assert count_freq(source) == expected


@pytest.mark.parametrize(
    "source, top, expected",
    [
        ({"a":3,"b":2,"c":1}, 2, [("a",3), ("b",2)]),
        ({"aa":2,"bb":2,"cc":1}, 5, [("aa",2), ("bb",2), ("cc",1)]),
    ],
)
def test_top_n_tie_breaker(source, top, expected):
    assert top_n(source, top) == expected
```
### Проведение быстрого теста
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/1.1.PNG)
### Проверка покрытия
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/1.2.PNG)
## **Задание Б**
### Код задания Б
```python
import pytest

# from src.lib.text import normalize, tokenize, count_freq, top_n # Не работает, пишет - нет модуля src
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Добавили путь в папку с функциями
from src.lab05.json_csv import json_to_csv, csv_to_json


# Проверка функции json_to_csv
@pytest.mark.parametrize(  # Создаём параметрайз с 3 запусками тестов
    "path_in, path_out, expected",  # Получаем ссылку исходный файл, на файл записи и ожидаемый вывод
    [
        (
            "././data/samples/people.json",
            "././data/out/people07.csv",
            None,
        ),  # Если ошибок нет, функция ничего не выдаст
        (
            "././data/samples/pustoy07.json",
            "././data/out/pustoy07.csv",
            ValueError,
        ),  # Если исходный файл пустой, ожидаем ошибку ValueError
        (
            "././data/samples/net_fayla07.json",
            "././data/out/net_fayla07.csv",
            FileNotFoundError,
        ),  # Если исходный файл не существует, ожидаем FileNotFoundError
    ],
)
def test_json_to_csv_basic(path_in, path_out, expected):
    if expected is None:  # Если ожидаемое поведение — тест успешно пройден
        assert json_to_csv(path_in, path_out) == expected
    else:  # Если ожидаем ошибку:
        with pytest.raises(expected):  # Совместно с модулем исключения ошибок
            json_to_csv(
                path_in, path_out
            )  # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден


# Проверка функции csv_to_json
@pytest.mark.parametrize(
    "path_in, path_out, expected",  # Получаем ссылку исходный файл, на файл записи и ожидаемый вывод
    [
        (
            "././data/samples/people1.csv",
            "././data/out/people07.json",
            None,
        ),  # Если ошибок нет, функция ничего не выдаст
        (
            "././data/samples/pustoy07.csv",
            "././data/out/pustoy07.json",
            ValueError,
        ),  # Если исходный файл пустой, ожидаем ошибку ValueError
        (
            "././data/samples/net_fayla07.csv",
            "././data/out/net_fayla07.json",
            FileNotFoundError,
        ),  # Если исходный файл не существует, ожидаем FileNotFoundError
    ],
)
def test_csv_to_json_basic(path_in, path_out, expected):
    if expected is None:  # Если получено ожидаемое поведение — тест успешно пройден
        assert csv_to_json(path_in, path_out) == expected
    else:  # Если ожидаем ошибку:
        with pytest.raises(expected):  # Совместно с модулем исключения ошибок
            csv_to_json(
                path_in, path_out
            )  # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден


import json
import csv
from pathlib import Path


# Проверка функции json_to_csv
def test_json_to_csv_roundtrip(tmp_path: Path):
    src = (
        tmp_path / "people.json"
    )  # Определение пути временного файла для json-данных с помощью фикстуры tmp_path
    dst = (
        tmp_path / "people.csv"
    )  # Определение пути временного файла для csv-данных с помощью фикстуры tmp_path
    data = [  # Тестовые данные
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )  # Преобразование списка словарей в строку формата json и сохранение её в файле 'src'
    json_to_csv(
        str(src), str(dst)
    )  # Вызыаваем функцию преобразования json в csv и передаём ей путь к источнику и месту назначения

    with dst.open(
        encoding="utf-8"
    ) as f:  # Читаем преобразованный csv-файл с помощью DictReader и получаем все строки в списке
        rows = list(csv.DictReader(f))

    assert len(rows) == 2  # Проверяем количество полученных записей
    assert {"name", "age"} <= set(
        rows[0].keys()
    )  # Проверяем наличие полей "name" и "age" в первой строке csv


# Проверка функции csv_to_json
def test_csv_to_json_roundtrip(tmp_path: Path):
    src = (
        tmp_path / "people.csv"
    )  # Определение пути временного файла для csv-данных с помощью фикстуры tmp_path
    dst = (
        tmp_path / "people.json"
    )  # Определение пути временного файла для json-данных с помощью фикстуры tmp_path
    data = [  # Тестовые данные
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    x = data[0].keys()  # Сохраняем изначальный порядок колонок
    with src.open("w", encoding="utf-8") as fc:
        writer = csv.DictWriter(
            fc, fieldnames=x, extrasaction="raise"
        )  # Переменная для удобной записи (файл для записи, порядок колонок, вывод ошибки если ключ не найден)
        writer.writeheader()
        writer.writerows(data)
    with src.open("r", encoding="utf-8") as fc:  # Открываем файл csv в режиме записи
        reader = csv.DictReader(fc)  # Записываем чтение в переменную
        data = []  # Создаём переменную для хранения словарей
        for row in reader:  # Для каждого словаря
            data.append(row)  # записываем его в список
    with dst.open("w", newline="", encoding="utf-8") as fj:  # Открываем json файл
        json.dump(
            data, fj, ensure_ascii=False, indent=2
        )  # Записываем в него список словарей, выводя только ASCII символы, отступ уровня важности равен 2

    assert len(data) == 2  # Проверяем количество полученных записей
    assert {"name", "age"} <= set(
        data[0].keys()
    )  # Проверяем наличие полей "name" и "age" в первой строке csv
```
### Проведение быстрого теста задания Б1
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/2.1.PNG)
### Проверка покрытия Б1
![05](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/2.2.PNG)
### Проведение быстрого теста задания Б2
![06](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/2.3.PNG)
### Проверка покрытия Б2
![07](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/2.4.PNG)
## **Проверка на соответствие black**
![08](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab07/2.5.1.PNG)