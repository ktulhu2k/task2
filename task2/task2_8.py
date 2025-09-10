try:
    num = 10 / float(input("Число:"))
    print(num)
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except ValueError:
    print("Ошибка: введите число, а не строку!")
finally:
    print("Программа завершена")