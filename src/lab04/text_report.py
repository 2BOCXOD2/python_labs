import sys
import os
from pathlib import Path
sys.path.insert(0, os.path.join(sys.path[0], '../lib')) # Добавили путь в папку с функциями
from io_txt_csv import write_csv
import text # normalize, tokenize, count_freq, top_n
path_in = "././data/lab04/input.txt"
if Path(path_in).exists(): # Проверяем наличие входного файла
    # path = input()
    with open(path_in, mode="r", newline='', encoding='utf-8') as f:
        st = f.read()
        top = 5
        a = text.normalize(st, casefold=True, yo2e=True) # Форматируем текст
        a = text.tokenize(a) # Убираем лишние символы
        a = text.count_freq(a) # Формируем словарь
        a = text.top_n(a, 5) # Формируем Топ
        print(a)
        z = []
        for item in a:
            z.append(item)
        write_csv(z, "././data/lab04/report.csv", ("Слово", "Частота"))
        print(f"Всего слов: {len(st.split())}")
        print(f"Уникальных слов: {len(a)}")
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
else:
    raise FileNotFoundError # Если файла нет - ошибка
