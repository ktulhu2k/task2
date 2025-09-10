for i in range(1, 6):
    print(i * i)

password = ""
while password != "1234":
    password = input("Введите пароль: ")
else:
    print("Успешный вход")