# **Лабораторная работа №8**
## **serialize**
### Код serialize
```python
import json
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str):
    with open(path, "w", encoding="utf-8") as f: # Создаём и открываем файл
        data = [] # Сохраняем студентов в переменную
        for student in students:
            data.append(student.to_dict())
        json.dump(data, f, ensure_ascii=False, indent=2) # Сохраняем список студентов в файле .json


def students_from_json(path: str) -> List[Student]:
    with open(path, "r", encoding="utf-8") as f: # Открываем файл
        data = json.load(f) # Загружаем список студентов из файла .json
        spisok_studentov = []
        for i in data:
            spisok_studentov.append(Student.from_dict(i))
        return spisok_studentov # Возвращаем список студентов





if __name__ == "__main__": # Запуск программы
    students_list = [ # Создание списка студентов
        Student(fio="Иванов И.И.", birthdate="1998-03-15", group="ПП-11", gpa=8.5),
        Student(fio="Петрова А.А.", birthdate="2000-05-23", group="ПП-12", gpa=9.2),
        Student(fio="Смирнов К.К.", birthdate="1999-11-10", group="ПП-13", gpa=7.8)
    ]

    
    students_to_json(students_list, "./data/lab08/students_input.json") # Экспортируем список студентов в JSON-файл

    
    loaded_students = students_from_json("./data/lab08/students_output.json") # Импортируем объекты обратно из JSON-файла

    
    for stud in loaded_students: # Выводим информацию о загруженных объектах
        print(stud)
```
### Результат проверки функционала
![01]()

### students_input
![02]()
### students_output
![03]()

## **models**
### Код models
```python
from dataclasses import dataclass
import datetime
from datetime import date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        # Проверяем правильность формата даты и диапазон оценки
        try:
            dt_obj = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Ошибка в формате даты {self.birthdate}: должно быть 'ГГГГ-ММ-ДД'") from e
            
        if not (0 <= self.gpa <= 10):
            raise ValueError("Средняя оценка должна находиться в диапазоне от 0 до 10.")
    
    def age(self) -> int:
        """Возвращает возраст студента"""
        birthday = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        years_diff = today.year - birthday.year
        is_before_birthday = (today.month, today.day) < (birthday.month, birthday.day)
        return years_diff - int(is_before_birthday)

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        """Создает экземпляр класса из словаря"""
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"])
        )

    def __str__(self):
        """Строковое представление объекта"""
        return f"{self.fio}, группа {self.group}, средний балл {self.gpa:.2f}"
```
### Проведение быстрого теста задания Б2
![04]()