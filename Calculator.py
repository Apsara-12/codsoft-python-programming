def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    """Main function to run the calculator."""
    while True:
        print("\nSimple Calculator")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result is: {result}")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
