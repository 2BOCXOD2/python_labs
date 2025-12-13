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
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab08/1%20Сериалайз%20с%20выводом.PNG)

### students_input
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab08/2%20Студенты%20инпут%20джейсон.PNG)
### students_output
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab08/3%20Студенты%20оутпут%20джейсон.PNG)

## **models**
### Код models
```python
from dataclasses import dataclass
import datetime
from datetime import date


@dataclass # Автоматически генерирует специальные методы для классов, ориентированных на хранение данных, что сокращает шаблонный код.
class Student: # Создаём класс
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try: # Проверяем правильность формата даты и диапазон оценки
            dt_obj = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        except ValueError as e:
            raise ValueError(f"Ошибка в формате даты {self.birthdate}: должно быть 'ГГГГ-ММ-ДД'") from e
            
        if not (0 <= self.gpa <= 10): # Проверка правильности оценки
            raise ValueError("Средняя оценка должна находиться в диапазоне от 0 до 10.")
    
    def age(self) -> int: # Функция подсчёта возраста
        birthday = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d").date() # Записываем дату в переменную для удобного сравнения
        today = date.today() # Получаем сегодняшнюю дату
        years_diff = today.year - birthday.year # Вычисляем разницу в годах
        is_before_birthday = (today.month, today.day) < (birthday.month, birthday.day) # Проверка наступления дня рождения
        return years_diff - int(is_before_birthday) # Возвращаем число полных лет

    def to_dict(self) -> dict: # self указывает на объект, с которым работает функция
        return { # Преобразуем объект в словарь
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls( # Создает экземпляр класса из словаря
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=float(d["gpa"])
        )

    def __str__(self): # Представляем объект как строку
        return f"{self.fio}, группа {self.group}, средний балл {self.gpa:.2f}, возраст {self.age()} лет"
```
### models.py
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab08/4%20Модельс.PNG)


