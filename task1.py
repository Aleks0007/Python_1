num = int(input("Введите трёхзначное число: "))

digit_sum = int(num / 100) + int(num / 10) % 10 + num % 10
print(f'Сумма цифр: {digit_sum}')