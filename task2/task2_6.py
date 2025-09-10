command = input("Комманда: ")

match command:
    case "start":
        print("Запуск")
    case "stop":
        print("Остановка")
    case "pause":
        print("Пауза")
    case _:
        print("Неизвестная команда")