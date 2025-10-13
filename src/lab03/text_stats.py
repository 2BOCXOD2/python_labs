import sys
import os
sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
import text # normalize, tokenize, count_freq, top_n

s = "Привет, мир! Привет!!!"
# s = input() # Если нужно вводить через терминал
top = 5
a = text.normalize(s, casefold=True, yo2e=True) # Форматируем текст
a = text.tokenize(a) # Убираем лишние символы
a = text.count_freq(a) # Формируем словарь
print(f"Всего слов: {len(s.split())}")
print(f"Уникальных слов: {len(a)}")
a = text.top_n(a, 5) # Формируем Топ
print('Топ-5:')
#for x, y in a: # Выводим Топ
#    print(f"{x}: {y}")
print("______________________") # Выводим данные красиво
max_len = 5 # Минимальная ширина столбца "Слово"
for r, t in a: # Поиск максимальной длины слова
    max_len = max(max_len, len(r))
print(f"Слово{" " * (max_len - 4)}| Частота") # Красиво выводим слово и частоту ровными столбцами
print("----------------------")
for x, y in a: # Выводим Топ красиво
    print(f"{x}{" " * (max_len - len(x) + 1)}| {y}") #Красиво выводим слово и частоту ровными столбцами
