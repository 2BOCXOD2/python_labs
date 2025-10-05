m = int(input("Минуты: "))
dd = hh // 24
hh = m // 60
mm = m % 60
hh = hh % 24
print(f"{hh}:{mm}")