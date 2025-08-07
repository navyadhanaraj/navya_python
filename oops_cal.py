
def main():
    print("Simple OOP Calculator")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        calc = Calculator(a, b) # type: ignore

        if operation == '+':
            print("Result:", calc.add())
        elif operation == '-':
            print("Result:", calc.subtract())
        elif operation == '*':
            print("Result:", calc.multiply())
        elif operation == '/':
            print("Result:", calc.divide())
        else:
            print("Invalid operation.")

    except ValueError:
        print("Please enter valid numbers.")


if __name__ == "__main__":
    main()

