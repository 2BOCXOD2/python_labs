
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

# textt = "   \nЕеЁё   \rАБвгД   \t12(%№?*)?;         "
# print(normalize(textt, casefold=True, yo2e=True))

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
# texxt = "emoji 😀 не слово"
# print(tokenize(texxt))

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
    for i in range(n_top): # Вывод топа
        otv_1.append(otv[i])
    return otv_1
# spisok = ["bb","aa","bb","aa","cc"]
# n = 2
# print(count_freq(spisok))
# print(top_n(count_freq(spisok), n))
