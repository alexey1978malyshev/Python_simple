# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.#
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# ...
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2

n = int(input("Введите количество монет: "))
i = 0
count_0 = 0
count_1 = 0
out_str = ''
while i < n:
    v = int(input('Введите положение монеты: '))
    if v == 1:
        count_1 += 1
    if v == 0:
        count_0 += 1
    else:
        print("Значение неверно. Попробуйте снова")
        break
    print(f"Положение монеты {i}: {v}")
    out_str += str(v) + ' '
    i += 1
min_count = min(count_1, count_0)
print(out_str)
print(f"Кол-во монет, чтобы перевернуть: {min_count}")
