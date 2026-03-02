def main():
    print("Hello from src/main.py!")
    print("IT changed")

    a = 7
    b = 3
    print(f"{a} + {b} = {a + b}")

    if (a + b) % 2 == 0:
        print("Сумма чётная")
    else:
        print("Сумма нечётная")


if __name__ == "__main__":
    main()
