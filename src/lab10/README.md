# **Лабораторная работа №9**
## **structures**
### Код structures
```python
from collections import deque

class Stack:
    def __init__(self):
        self._data = []  # Внутреннее хранилище для элементов стека

    def push(self, item):
        self._data.append(item)  # Элемент добавляется в конец списка

    def pop(self):
        if self.is_empty():  # Проверка на пустоту стека
            raise IndexError("Стек пуст")  # Бросаем исключение
        return self._data.pop()  # Удаляем и возвращаем верхний элемент

    def peek(self):
        if self.is_empty():  # Проверка на пустоту стека
            return None  # Возврат None, если стек пуст
        return self._data[-1]  # Верхний элемент стека

    def is_empty(self) -> bool:
        return len(self._data) == 0  # Эффективная проверка на пустоту


class Queue:
    def __init__(self):
        self._data = deque()  # Использование deque для оптимальной работы очереди

    def enqueue(self, item):
        self._data.append(item)  # Добавляем элемент в конец очереди

    def dequeue(self):
        if self.is_empty():  # Проверка на пустоту очереди
            raise IndexError("Очередь пуста")  # Исключение при попытке извлечения из пустой очереди
        return self._data.popleft()  # Извлекаем элемент из начала очереди

    def peek(self):
        if self.is_empty():  # Проверка на пустоту очереди
            return None  # Вернём None, если очередь пуста
        return self._data[0]  # Первый элемент очереди

    def is_empty(self) -> bool:
        return len(self._data) == 0  # Проверка на пустоту


"""Проверка функционала"""
# Создание экземпляра стэка
stack = Stack()
print("\n--- Testing Stack ---")
stack.push(10)
stack.push(20)
print("Peek:", stack.peek())  # Ожидаемый вывод: Peek: 20
item = stack.pop()
print("Popped:", item)       # Ожидаемый вывод: Popped: 20
print("Is empty?", stack.is_empty())   # Ожидаемый вывод: Is empty? False
stack.pop()
print("Is empty after last pop?", stack.is_empty())   # Ожидаемый вывод: Is empty after last pop? True

# Создание экземпляра очереди
queue = Queue()
print("\n--- Testing Queue ---")
queue.enqueue('A')
queue.enqueue('B')
print("Dequeue:", queue.dequeue())     # Ожидаемый вывод: Dequeue: A
print("Peek:", queue.peek())           # Ожидаемый вывод: Peek: B
print("Is empty?", queue.is_empty())   # Ожидаемый вывод: Is empty? False
queue.dequeue()
print("Is empty after last dequeue?", queue.is_empty())   # Ожидаемый вывод: Is empty after last dequeue? True

```

### Результат проверки функционала structures
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab10/1%20Проверка%20первого%20файла.PNG)


## **linked_list**
### Код linked_list
```python
class Node:
    def __init__(self, value, next=None):
        self.value = value  # Значение узла
        self.next = next  # Следующий узел

    # Класс Node теперь имеет красивый вывод строки благодаря переопределенному методу __repr__, который возвращает строку вида [value].
    def __repr__(self):  # Представление отдельного узла
        return f"[{self.value}]"


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Голова списка
        self._size = 0  # Количество элементов в списке

    def append(self, value):
        """Добавляет элемент в конец списка."""
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
        """Добавляет элемент в начало списка."""
        new_node = Node(value, next=self.head)
        self.head = new_node
        self._size += 1  # Увеличение размера списка

    def insert(self, idx, value):
        """
        Вставляет элемент по указанному индексу.
        
        :param idx: Индекс для вставки
        :param value: Значение нового элемента
        """
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
        """Удаляет первое вхождение указанного значения."""
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
            current = current.next

    def remove_at(self, idx):
        """Удаляет элемент по индексу."""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} выходит за рамки списка.")
        
        if idx == 0:
            self.head = self.head.next
            self._size -= 1
            return
        
        prev = None
        current = self.head
        position = 0
        while current and position < idx:
            prev = current
            current = current.next
            position += 1
        
        prev.next = current.next
        self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size  # Возвращаем количество элементов

    # Метод __repr__ в классе SinglyLinkedList формирует цепочку узлов, соединяя их стрелочками и завершал "None".
    def __repr__(self):
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
```

### Результат проверки функционала linked_list
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab10/2%20Проверка%20второго%20файла.PNG)


### Результат проверки функционала linked_list красивый вывод со звёздочкой
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab10/3%20Красивый%20вывод.PNG)

