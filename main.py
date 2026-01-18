def gcd(a, b):
    """Вычисляет НОД двух чисел по алгоритму Евклида."""
    while b:
        a, b = b, a % b
    return abs(a)


def main():
    print("Нахождение НОД двух чисел")
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = gcd(a, b)
        print(f"НОД({a}, {b}) = {result}")
    except ValueError:
        print("Ошибка! Введите целые числа.")


if __name__ == "__main__":
    main()