# **Лабораторная работа №3**
## **Задание A**
### Код задания №1
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if type(text) == str:
        if casefold == True: # Если включено, делает все буквы строчными
            text = text.casefold()
        if yo2e == True: # Если включено, делает все Ё/ё буквами Е/е
            text = text.replace("ё", "е")
            text = text.replace("Ё", "Е")
        text = text.split() # Убирает лишние пробелы
        new_text = ""
        lenn = len(text)
        for i in range(lenn): # Превращает список назад в строку
            if i < lenn - 1:
                new_text = f"{new_text + text[i]} "
            else:
                new_text = f"{new_text + text[i]}"
        new_text = new_text.replace("\n", '') # Удаляет все лишние символы
        new_text = new_text.replace("\r", '')
        new_text = new_text.replace("\t", '')
        return new_text
    else:
        raise TypeError

textt = "   \nЕеЁё   \rАБвгД   \t12(%№?*)?;         "
print(normalize(textt, casefold=True, yo2e=True))
```
Скриншот задания №1
![01](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab03/1.1.PNG)
### Код задания №2
```
def tokenize(text: str):
    if type(text) == str:
        alf = ",.!_;:?😀" # Символы-пробелы
        text = text.split()
        lenn = len(text)
        new_text = ''
        for i in range(lenn): # Удалили пробелы и переводим в тип строки
            if i < lenn - 1:
                new_text = f"{new_text + text[i]} "
            else:
                new_text = f"{new_text + text[i]}"
        for a in alf: # Удаляем символы-пробелы и переводим в тип строки
            text = new_text
            text = text.split(a)
            lenn = len(text)
            new_text = ""
            for j in range(lenn):
                if j < lenn - 1:
                    new_text = f"{new_text + text[j]} "
                else:
                    new_text = f"{new_text + text[j]}"
        new_text = new_text.split()
        return new_text
    else:
        raise TypeError
texxt = "emoji 😀 не слово"
print(tokenize(texxt))
```
Скриншот задания №2
![02](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab03/1.2.PNG)
### Код заданий №3 и №4
```
def count_freq(dannye):
    new_dannye = []
    for i in dannye:
        if i in new_dannye:
            pass
        else:
            new_dannye.append(i)
    slovar = {}
    for z in new_dannye:
        col = dannye.count(z) # Количество вхождений
        slovar[z] = col
    return slovar
def top_n(dictt, n_top):
    a = []
    for key, value in dictt.items():
        a.append((key, value))
    otv = a.sort() # Сортировка по алфавиту
    otv = sorted(a, key = lambda x: (x[1]), reverse=True) # Сортировка по частоте
    otv_1 = []
    if n_top > len(dictt): # Проверка длины
        for i in range(len(dictt)): # Формирование топа
            otv_1.append(otv[i])
    else:
        for i in range(n_top): # Формирование топа
            otv_1.append(otv[i])
    return otv_1
spisok = ["bb","aa","bb","aa","cc"]
n = 2
print(count_freq(spisok))
print(top_n(count_freq(spisok), n))
```
Скриншот заданий №3 и №4
![03](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab03/1.3%2C4.PNG)
## **Задание B**
### Код задания B
```
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
import text # normalize, tokenize, count_freq, top_n

s = "Привет, мир! Привет!!!"
#s = input() # Если нужно вводить через терминал
top = 5
a = text.normalize(s, casefold=True, yo2e=True) # Форматируем текст
a = text.tokenize(a) # Убираем лишние символы
a = text.count_freq(a) # Формируем словарь
print(f"Всего слов: {len(s.split())}")
print(f"Уникальных слов: {len(a)}")
a = text.top_n(a, 5) # Формируем Топ
print('Топ-5:')
for x, y in a: # Выводим Топ
    print(f"{x}: {y}")
```
Скриншот задания B
![04](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab03/2.1.PNG)
## **Задание Б**
### Код задания Б
```
import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
import text # normalize, tokenize, count_freq, top_n

s = "Привет, мир! Привет!!!"
#s = input() # Если нужно вводить через терминал
top = 5
a = text.normalize(s, casefold=True, yo2e=True) # Форматируем текст
a = text.tokenize(a) # Убираем лишние символы
a = text.count_freq(a) # Формируем словарь
print(f"Всего слов: {len(s.split())}")
print(f"Уникальных слов: {len(a)}")
a = text.top_n(a, 5) # Формируем Топ
print('Топ-5:')
print("______________________") # Выводим данные красиво
max_len = 5 # Минимальная ширина столбца "Слово"
for r, t in a: # Поиск максимальной длины слова
    max_len = max(max_len, len(r))
print(f"Слово{" " * (max_len - 4)}| Частота") # Красиво выводим слово и частоту ровными столбцами
print("----------------------")
for x, y in a: # Выводим Топ красиво
    print(f"{x}{" " * (max_len - len(x) + 1)}| {y}") #Красиво выводим слово и частоту ровными столбцами
```
![05](https://github.com/2BOCXOD2/python_labs/blob/main/img/lab03/2.2.PNG)