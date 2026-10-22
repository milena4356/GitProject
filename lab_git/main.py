def main():
    print("Простой калькулятор")
    try:
        first = int(input("Введите первое целое число: "))
        second = int(input("Введите второе целое число: "))
    except ValueError:
        print("Ошибка: нужно ввести целые числа.")
        return

    print(f"Сумма чисел: {first + second}")


if __name__ == "__main__":
    main()
