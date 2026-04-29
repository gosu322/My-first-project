import random



print("Добро пожаловать в числовую угадайку")


def is_valid(value):
    if value.isdigit():
        return 1 <= int(value) <= 100
    return False


game = input("Хотите сыграть?(да/нет)\n")

while game == "да":
    number = random.randint(1, 100)
    counter = 0
    print("Я загадал целое число от 1 до 100")
    while True:
        user_input = input("Введите целое число от 1 до 100\n")

        if not is_valid(user_input):
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue

        user_num = int(user_input)
        counter += 1
        if user_num < number:
            print("Ваше число меньше загаданного, попробуйте ещё разок")
        elif user_num > number:
            print("Ваше число больше загаданного, попробуйте ещё разок")
        else:
            print("Вы угадали, поздравляем!")
            print(f"Попыток сделано: {counter}")
            break

    game = input(
        "Спасибо, что сыграли в числовую угадайку! Хотите сыграть ещё?(да/нет)\n"
    )
    if game == "нет":
        print("Очень жаль. Ждём вас снова!")
            
        
