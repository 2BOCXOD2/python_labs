from pathlib import exists
def read_text(path: str, encoding: str = "utf-8"):
    if type(path) == str:
        if encoding == "utf-8":
            if exists(path):
                ssilka = path
                f = open(path, "r")
                st = f.read()
                f.close()
                return st
            else:
                raise FileNotFoundError
        else:
            raise UnicodeDecodeError
    else:
        raise ValueError

print(read_text("././data/lab04/input.txt", "utf-8"))



# f = open("C:/Users/GN/Desktop/python_labs/data/lab04/input.txt", "r")
# f = open("././data/lab04/input.txt", "r")
# res = f.read()
# print(res)
# f.close()