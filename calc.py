def calc(a, b):
    x = a + b
    y = a - b
    z = a * b
    print(f"Сумма: {x}")
    print(f"Разность: {y}")
    print(f"Произведение: {z}")
    return x, y, z

# Используем функцию
num1 = 10
num2 = 5
result1, result2, result3 = calc(num1, num2)

print(f"Результат 1: {result1}")
print(f"Результат 2: {result2}")
print(f"Результат 3: {result3}")

# Ещё одна плохая переменная
x = 100
print(f"x = {x}")