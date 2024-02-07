def sum_range(a, b):
    if a > b:
        return 0  # Базовый случай: если a больше b, возвращаем 0
    else:
        return a + sum_range(a + 1, b)  # Рекурсивный случай: добавьте a к сумме диапазона от a+1 до b

a = 3
b = 7
print(sum_range(a, b))