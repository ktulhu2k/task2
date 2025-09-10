num = int(input("Число: "))
result = "even" if num % 2 == 0 else "odd"
print(result)

if (str := input("Введите строку: ")).isdigit():
    print("Это число")