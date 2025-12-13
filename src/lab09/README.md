# **Лабораторная работа №9**
## **group**
### Код group
```python
import csv
from typing import List, Dict
from pathlib import Path
import sys
import os
sys.path.append(os.path.abspath('..'))
from src.lab08.models import Student


class Group:
    def __init__(self, storage_path: str):
        """
        Инициализирует группу студентов и проверяет наличие файла хранения.
        
        :param storage_path: путь к файлу CSV для сохранения данных
        """
        self.path = Path(storage_path)
        if not self.path.exists(): # Если пути не существует, создаём новфй файл
            with open(self.path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa']) # И задаём названия колонок
    
    def _read_all(self) -> List[Dict[str, str]]:
        """
        Читает строки из CSV-файла и возвращает список записей.
        
        :return: Список словарей с полями студента (ФИО, дата рождения, группа, gpa).
        """
        result = []
        try:
            with open(self.path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file) # Читаем все записи
                for row in reader:
                    result.append(row)
        except FileNotFoundError:
            pass
        return result
    
    def list(self) -> List[Student]:
        """
        Возвращает список объектов типа Student из хранилища.
        
        :return: Список объектов Student.
        """
        students = []
        rows = self._read_all()
        for row in rows:
            students.append( # Добавляем всех студентов в виде объектов Student
                Student(fio=row['fio'], birthdate=row['birthdate'], group=row['group'], gpa=float(row['gpa']))
            )
        return students

    def add(self, student: Student):
        """
        Добавляет нового студента в файл.
        
        :param student: объект типа Student для добавления
        """
        # Получаем текущие данные
        current_data = self._read_all()
        
        # Добавляем нового студента
        current_data.append({
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': student.gpa
        })
        
        # Перезаписываем файл с новыми данными
        with open(self.path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])  # заголовочная строка
            writer.writerows([
                [row['fio'], row['birthdate'], row['group'], row['gpa']]
                for row in current_data
            ])

    def find(self, substr: str) -> List[Student]:
        """
        Поиск студентов по частичному совпадению ФИО.
        
        :param substr: Подстрока для поиска среди ФИО студентов
        :return: Список найденных студентов
        """
        found_students = [] # Создаём список подходящих студентов
        rows = self._read_all() # Получаем все записи
        for row in rows:
            if substr.lower() in row['fio'].lower(): # Если есть совпадение
                found_students.append( # Добавляем запись
                    Student(fio=row['fio'], birthdate=row['birthdate'], group=row['group'], gpa=float(row['gpa']))
                )
        return found_students # Выводим все подходящие записи

    def remove(self, fio: str):
        """
        Удаляет запись о студенте по указанному ФИО.
        
        :param fio: Полное ФИО студента для удаления
        """
        rows = self._read_all() # Получаем записи
        updated_rows = [row for row in rows if row['fio'] != fio] # Получаем ФИО студентов
        with open(self.path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if updated_rows:  # Только если есть хотя бы одна строка
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])  # Заголовочная строка
            writer.writerows([[r['fio'], r['birthdate'], r['group'], r['gpa']] for r in updated_rows])

    def update(self, fio: str, **fields):
        """
        Обновляет поля записи о студенте по ФИО.
        
        :param fio: ФИО студента для обновления
        :param fields: Словарь обновляемых полей и значений
        """
        rows = self._read_all() # Получаем записи
        updated_rows = []
        for row in rows:
            if row['fio'] == fio:
                for key, value in fields.items():
                    row[key] = value
            updated_rows.append(row)
        with open(self.path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            if updated_rows:  # Только если есть хотя бы одна строка
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])  # Заголовочная строка
            writer.writerows([[r['fio'], r['birthdate'], r['group'], r['gpa']] for r in updated_rows])
        
    def stats(self) -> dict:
        """
        Анализирует данные о студентах и возвращает сводную статистику.
        
        :return: Словарь с общей статистикой по группе студентов.
        """
        data = self._read_all()
        count = len(data)
        
        # Определение минимального и максимального GPA
        gpas = [float(student['gpa']) for student in data]
        min_gpa = min(gpas) if gpas else None
        max_gpa = max(gpas) if gpas else None
        avg_gpa = sum(gpas) / len(gpas) if gpas else None
        
        # Статистика по группам
        groups_count = {}
        for student in data:
            group_name = student['group']
            groups_count[group_name] = groups_count.get(group_name, 0) + 1
        
        # Топ-5 лучших студентов по среднему баллу
        top_students = sorted(data, key=lambda x: float(x['gpa']), reverse=True)[:5]
        top_5_students = [{
            "fio": student["fio"],
            "gpa": float(student["gpa"])
        } for student in top_students]
        
        return {
            "count": count,
            "min_gpa": min_gpa,
            "max_gpa": max_gpa,
            "avg_gpa": avg_gpa,
            "groups": groups_count,
            "top_5_students": top_5_students
        }

if __name__ == "__main__":
    # Создаем экземпляр класса Group
    group_storage = './data/lab09/students.csv'
    my_group = Group(group_storage)

    # Тестируем метод .add(), добавляем двух новых студентов
    new_student_1 = Student("Иванов Иван Иванович", "1999-01-01", "1А", 4.5)
    new_student_2 = Student("Петрова Анна Сергеевна", "2000-05-15", "2Б", 4.8)
    my_group.add(new_student_1)
    my_group.add(new_student_2)

    # Проверяем список студентов методом .list()
    print("\nСписок студентов:")
    all_students = my_group.list()
    for st in all_students:
        print(st.__dict__)

    # Тестируем метод .find(), ищем студента Иванов
    search_result = my_group.find("Иванов")
    print("\nРезультат поиска по фамилии \"Иванов\":")
    for st in search_result:
        print(st.__dict__)

    # Используем метод .update(), меняем группу Иванова Ивана
    my_group.update("Иванов Иван Иванович", group="3В")

    # Повторно выводим список студентов, чтобы увидеть изменения
    print("\nОбновленный список студентов после изменения группы:")
    updated_students = my_group.list()
    for st in updated_students:
        print(st.__dict__)

    # Применяем метод .remove(), удаляем Петровой Анну
    my_group.remove("Петрова Анна Сергеевна")

    # Снова выводим список, чтобы удостовериться, что удаление произошло
    print("\nФинальный список студентов после удаления Петровой Анны:")
    final_students = my_group.list()
    for st in final_students:
        print(st.__dict__)
    
    # Проверка работоспособности статистики
    print("\nСтатистика по студентам:")
    my_group = Group('./data/lab09/students.csv')
    result_stats = my_group.stats()

    print("Статистика по студентам:")
    print(f"Количество студентов: {result_stats['count']}")
    print(f"Минимальный GPA: {result_stats['min_gpa']:.2f}")
    print(f"Максимальный GPA: {result_stats['max_gpa']:.2f}")
    print(f"Средний GPA: {result_stats['avg_gpa']:.2f}\n")

    print("Группы и количество студентов:")
    for group, count in result_stats['groups'].items():
        print(f"{group}: {count}")

    print("\nТоп-5 студентов по успеваемости:")
    for student in result_stats['top_5_students']:
        print(f"{student['fio']} | Средний балл: {student['gpa']:.2f}")


# python -m src.lab09.group



# python -m src.lab09.group
```
### Результат проверки функционала 1
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab09/1%20Итог.PNG)

### Результат проверки функционала 2 *
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab09/2%20Итог.PNG)

