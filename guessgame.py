import random
secret = random.randint(1, 100)

print("Я загадал число от 1 до 100. У вас 5 попыток.")

for attempt in range(1, 6):
    guess = int(input(f"Попытка {attempt}. Введите число: "))

    if guess == secret:
        print("Поздравляю! Вы угадали число!")
        break
    elif attempt == 3 and guess != secret:
        tens = secret // 10
        print(f"Не угадали. Подсказка: десятки загаданного числа — {tens}.")
        if guess < secret:
            print("Число больше.")
        else:
            print("Число меньше.")
    elif attempt < 5:
        if guess < secret:
            print("Число больше.")
        else:
            print("Число меньше.")
    else:
        print(f"Вы проиграли. Загаданное число было {secret}.")