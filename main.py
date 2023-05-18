n = int(input("Введите число: "))
i = 1
res = ""
while i <= n:
    simple = True
    j = 2
    while j < i:
        if i % j == 0:
            simple = False
        j += 1

    if simple:
        res = res + str(i) + ' '

    i += 1
print(f"Простые числа от 1 до {n}: {res}")

