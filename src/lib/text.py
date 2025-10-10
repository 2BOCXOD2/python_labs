'''
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if type(text) == str:
        if casefold == True:
            text = text.casefold()
        if yo2e == True:
            text = text.replace("ё", "е")
            text = text.replace("Ё", "Е")
        text = text.split()
        new_text = ""
        lenn = len(text)
        for i in range(lenn):
            if i < lenn - 1:
                new_text = f"{new_text + text[i]} "
            else:
                new_text = f"{new_text + text[i]}"
        new_text = new_text.replace("\n", '')
        new_text = new_text.replace("\r", '')
        new_text = new_text.replace("\t", '')
        return new_text
    else:
        raise TypeError

textt = "   \nЕеЁё   \rАБвгД   \t12(%№?*)?;         "
print(normalize(textt, casefold=True, yo2e=True))
'''

def tokenize(text: str):
    if type(text) == str:
        alf = ",.!_;:?"
        text = text.split()
        lenn = len(text)
        new_text = ''
        for i in range(lenn):
            if i < lenn - 1:
                new_text = f"{new_text + text[i]} "
            else:
                new_text = f"{new_text + text[i]}"

        return new_text
    else:
        raise TypeError

texxt = "привет мир"
print(tokenize(texxt))
print(123)

'''
        new_text_2 = ''
        for j in alf:
            new_text = new_text.split(j)
            new_lenn = len(new_text)
            for z in range(new_lenn):
                if z < new_lenn - 1:
                    new_text_2 = f"{new_text_2 + new_text[z]} "
                else:
                    new_text_2 = f"{new_text_2 + new_text[z]}"
'''
