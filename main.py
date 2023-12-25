def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print(f"НОД чисел {num1} и {num2} равен {euclidean_algorithm(num1, num2)}")
