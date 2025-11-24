import pytest
# from src.lib.text import normalize, tokenize, count_freq, top_n # Не работает, пишет - нет модуля src
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Добавили путь в папку с функциями
from src.lab05.json_csv import json_to_csv, csv_to_json

'''
@pytest.mark.parametrize(
    "path_in, path_out, expected",
    [
        ("././data/samples/people.json", "././data/out/people07.csv", None),
        ("././data/samples/pustoy07.json", "././data/out/pustoy07.csv", ValueError),
        ("././data/samples/net_fayla07.json", "././data/out/net_fayla07.csv", FileNotFoundError),
    ],
)
def test_json_to_csv_basic(path_in, path_out, expected):
    if expected is None: # Если ожидаемое поведение — тест успешно пройден
        assert json_to_csv(path_in, path_out) == expected
    else: # Если ожидаем ошибку:
        with pytest.raises(expected): # Совместно с модулем исключения ошибок
            json_to_csv(path_in, path_out) # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден

@pytest.mark.parametrize(
    "path_in, path_out, expected",
    [
        ("././data/samples/people1.csv", "././data/out/people07.json", None),
        ("././data/samples/pustoy07.csv", "././data/out/pustoy07.json", ValueError),
        ("././data/samples/net_fayla07.csv", "././data/out/net_fayla07.json", FileNotFoundError),
    ],
)
def test_csv_to_json_basic(path_in, path_out, expected):
    if expected is None: # Если получено ожидаемое поведение — тест успешно пройден
        assert csv_to_json(path_in, path_out) == expected
    else: # Если ожидаем ошибку:
        with pytest.raises(expected): # Совместно с модулем исключения ошибок
            csv_to_json(path_in, path_out) # Запускаем функцию. Если ошибка соответствует значению expected, тест пройден
'''


import json
import csv
from pathlib import Path

def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    with src.open("r", encoding="utf-8") as fc: # Открываем файл csv в режиме чтения
        reader = csv.DictReader(fc) # Записываем чтение в переменную
        data = [] # Создаём переменную для хранения словарей
        for row in reader: # Для каждого словаря
            data.append(row) # записываем его в список
    with dst.open("w", newline='', encoding="utf-8") as fj: # Открываем json файл
        json.dump(data, fj, ensure_ascii=False, indent=2) # Записываем в него список словарей, выводя только ASCII символы, отступ уровня важности равен 2

    assert len(data) == 2
    assert {"name", "age"} <= set(data[0].keys())