x = input("Введите число: ")
if x is None:
    print("x is None")
else:
    x = int(x)
    if 10 <= x <= 20:
        print("В диапазоне [10, 20]")
    else:
        print("Не в диапазоне [10, 20]")