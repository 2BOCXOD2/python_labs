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
for x, y in a: # Выводим Топ
    print(f"{x}: {y}")