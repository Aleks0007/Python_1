""" 
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? 
"""
# Допустим Х - число журавликов, сделанных Петей, соответственно у Серёжи тоже Х журавликов.
# Тогда Катя сделала (2Х * 2) журавликов
# Получим уравнение S = Х + Х + (2Х * 2) => S = 6Х => Х = S / 6

sum = int(input("Введите общее количество журавликов кратное шести: "))
if (sum % 6 == 0):
    petya = int(sum / 6)
    katya = petya * 2 * 2
    print(f'Петя: {petya}, Серёжа: {petya}, Катя: {katya}')
else:
    print('Введено неверное число!')