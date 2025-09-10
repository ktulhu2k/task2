number = float(input("Число: "))

# Проверяем положительное, отрицательное или ноль
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")

# Дополнительная проверка: делится ли на 2 и на 3 одновременно
if number % 2 == 0 and number % 3 == 0:
    print("Число делится и на 2, и на 3 одновременно")
else:
    print("Число НЕ делится и на 2, и на 3 одновременно")