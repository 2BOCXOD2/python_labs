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





"""
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0
"""