import random

counter = 0
number = random.randint(1, 100)
print("Добро пожаловать в числовую угадайку")


def is_valid(value):
    if value.isdigit():
        return 1 <= int(value) <= 100
    return False

game = input("Хотите сыграть?(да/нет)\n")
while game == "да":
    user_input = input("Введите целое число от 1 до 100\n")
    if not is_valid(user_input):
        print("А может быть всё-таки введем целое число от 1 до 100?")
        continue

    user_num = int(user_input)
    if user_num < number:
        print("Ваше число меньше загаданного, попробуйте ещё разок")
        counter += 1
    elif user_num > number:
        print("Ваше число больше загаданного, попробуйте ещё разок")
        counter += 1
    else:
        print("Вы угадали, поздравляем!")
        print(f'Попыток сделано: {counter}')
        game = input("Спасибо, что сыграли в числовую угадайку! Хотите сыграть ещё?(да/нет)\n")
        if game == "нет":
            print("Очень жаль. Ждём вас снова!")
            break
