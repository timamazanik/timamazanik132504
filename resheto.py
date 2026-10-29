try:
    n = int(input("Введите N: "))
except ValueError:
    print("Ошибка: введите целое число.")
    exit()

if n < 2:
    print("Ошибка: N должно быть не меньше 2.")
    exit()


numbers = {}

for i in range(2, n + 1):
    numbers[i] = True

# Решето Эратосфена
p = 2

while p * p <= n:
    if numbers[p]:
        # Удаляем кратные числа p
        for i in range(p * p, n + 1, p):
            numbers[i] = False

    p += 1

# Выводим простые числа
for number in numbers:
    if numbers[number]:
        print(number)