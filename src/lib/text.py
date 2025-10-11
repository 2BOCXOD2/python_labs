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
        for a in alf:
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
texxt = "по-настоящему круто"
print(tokenize(texxt))