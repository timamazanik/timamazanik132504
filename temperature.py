
text = input("Введите температуру: ")
number = float(text[:-1])
scale = text[-1]

if scale == "C":
    print(number * 9 / 5 + 32, "F")
else:
    print((number - 32) * 5 / 9, "C")