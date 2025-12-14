class Node: # Узел односвязного списка.
    def __init__(self, value, next=None):
        self.value = value  # Хранит значение текущего узла
        self.next = next  # Указатель на следующий узел в списке

    # Класс Node теперь имеет красивый вывод строки благодаря переопределенному методу __repr__, который возвращает строку вида [value].
    def __repr__(self):  # Представление отдельного узла
        return f"[{self.value}]"


class SinglyLinkedList:
    def __init__(self):
        self.head = None # Начальный узел списка (голова)
        self._size = 0 # Количество элементов в списке

    def append(self, value):
        """Добавляет элемент в конец списка."""
        new_node = Node(value) # Создаем новый узел с заданным значением
        if self.head is None: # Если список пуст
            self.head = new_node # Новый узел становится головой списка
        else:
            current = self.head # Начинаем с головы списка
            while current.next is not None: # Идем до последнего узла
                current = current.next
            current.next = new_node # Присоединяем новый узел в конце
        self._size += 1 # Увеличиваем размер списка

    def prepend(self, value):
        """Добавляет элемент в начало списка."""
        new_node = Node(value, next=self.head) # Создаем новый узел, указывая следующую ссылку на голову
        self.head = new_node # Устанавливаем новую голову списка
        self._size += 1  # Увеличение размера списка

    def insert(self, idx, value):
        """
        Вставляет элемент по указанному индексу.
        
        :param idx: Индекс для вставки
        :param value: Значение нового элемента
        """
        if idx < 0 or idx > self._size: # Проверка индекса на валидность
            raise IndexError(f"Неверный индекс {idx}") # Выбрасываем ошибку, если индекс неверный
            
        if idx == 0: # Если вставляем в начало
            self.prepend(value) # Используем метод добавления в начало
            return
        
        current = self.head # Начало списка
        position = 0 # Переменная для отслеживания текущей позиции
        while current and position < idx - 1: # Двигаемся до нужного места
            current = current.next
            position += 1
        
        new_node = Node(value, next=current.next) # Создаем новый узел
        current.next = new_node # Меняем связь предыдущего узла на новый
        self._size += 1  # Увеличение размера списка

    def remove_value(self, value):
        """Удаляет первое вхождение указанного значения."""
        if self.head is None: # Если список пуст
            return
        
        if self.head.value == value: # Если первый элемент равен искомому
            self.head = self.head.next # Просто меняем голову списка
            self._size -= 1 # Уменьшаем размер
            return
        
        prev = None # Предыдущий узел
        current = self.head # Текуций узел
        while current is not None: # Пока не дошли до конца
            if current.value == value: # Нашли нужный элемент
                prev.next = current.next # Обходим найденный узел
                self._size -= 1 # Уменьшаем размер
                break
            prev = current # Сохраняем предыдущий узел
            current = current.next # Переходим к следующему узлу

    def remove_at(self, idx):
        """Удаляет элемент по индексу."""
        if idx < 0 or idx >= self._size: # Проверка индекса на валидность
            raise IndexError(f"Индекс {idx} выходит за рамки списка.") # Выбрасываем ошибку, если индекс вне диапазона
        
        if idx == 0: # Если удаляем первый элемент
            self.head = self.head.next # Меняем голову списка
            self._size -= 1 # Уменьшаем размер
            return
        
        prev = None # Предыдущий узел
        current = self.head # Текуций узел
        position = 0 # Переменная для отслеживания текущей позиции
        while current and position < idx: # Двигаемся до нужного места
            prev = current
            current = current.next
            position += 1
        
        prev.next = current.next # Обходим найденный узел
        self._size -= 1 # Уменьшаем размер

    def __iter__(self):
        current = self.head # Начинаем с головы списка
        while current is not None: # Пока не дойдем до конца
            yield current.value # Генерируем текущее значение
            current = current.next # Переходим к следующему узлу

    def __len__(self):
        return self._size  # Возвращаем количество элементов в списке

    # Метод __repr__ в классе SinglyLinkedList формирует цепочку узлов, соединяя их стрелочками и завершал "None".
    def __repr__(self): # Формируем красивое представление
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current))
            current = current.next
        return " -> ".join(nodes + ["None"])
    
"""
    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"
"""

"""Проверка функционала"""
sll = SinglyLinkedList()
print("\n--- Testing Singly Linked List ---")
sll.append(1)
sll.prepend(2)
sll.insert(1, 3)
print("Current state of the list:", sll)      # Ожидаемый вывод: Current state of the list: SinglyLinkedList([2, 3, 1])
sll.remove_value(3)
print("After removing value 3:", sll)         # Ожидаемый вывод: After removing value 3: SinglyLinkedList([2, 1])
sll.remove_at(0)
print("After removing at index 0:", sll)      # Ожидаемый вывод: After removing at index 0: SinglyLinkedList([1])
print("Length of the list:", len(sll))        # Ожидаемый вывод: Length of the list: 1


# Проверка красивого вывода
sll = SinglyLinkedList()
sll.append('A')
sll.append('B')
sll.append('C')
print(sll)  # Выведет: [A] -> [B] -> [C] -> None


"""
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Голова списка
        self._size = 0  # Количество элементов в списке

    def append(self, value):
        #Добавляет элемент в конец списка.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1  # Увеличение размера списка

    def prepend(self, value):
        #Добавляет элемент в начало списка.
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1  # Увеличение размера списка

    def insert(self, idx, value):
        # Вставляет элемент по указанному индексу.
        
        # :param idx: Индекс для вставки
        # :param value: Значение нового элемента

        if idx < 0 or idx > self._size:
            raise IndexError(f"Неверный индекс {idx}")
            
        if idx == 0:
            self.prepend(value)
            return
        
        current = self.head
        position = 0
        while current and position < idx - 1:
            current = current.next
            position += 1
        
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1  # Увеличение размера списка

    def remove_value(self, value):
        # Удаляет первое вхождение указанного значения.
        if self.head is None:
            return
        
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return
        
        prev = None
        current = self.head
        while current is not None:
            if current.value == value:
                prev.next = current.next
                self._size -= 1
                break
            prev = current
            current = current
"""