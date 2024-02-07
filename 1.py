# #№1
def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))

# #№3
def print_stars(n):
    if n == 0:
        return
    print('*', end='')
    print_stars(n-1)

n = int(input("Enter a number: "))

print_stars(n)
