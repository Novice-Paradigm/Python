def input_number(message: str) -> float:
    try:
        number = float(input(message))
        return number
    except ValueError:
        print("Unsupported format for numbers!")
        exit(2)


if __name__ == '__main__':
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "**": lambda a, b: a ** b
    }
    print("Choose a operation: \n + for addition \n - for subtraction \n * for multiplication \n / for division \n ** for power")
    input_operation = input("Enter a operation: ")

    operation = operations.get(input_operation, None)
    if operation is None:
        print("Unsupported operation!")
        exit(1)

    number1 = input_number("Enter the first number: ")
    number2 = input_number("Enter the second number: ")

    print("Result: " + str(operation(number1, number2)))
