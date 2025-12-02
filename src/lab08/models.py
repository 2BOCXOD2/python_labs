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
    
