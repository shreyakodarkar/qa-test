def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            print("Result:", add(x, y))
        elif choice == "2":
            print("Result:", subtract(x, y))
        elif choice == "3":
            print("Result:", multiply(x, y))
        else:
            print("Result:", divide(x, y))
    else:
        print("Invalid choice, try again.")
        # done 
        hi how are you this is the end of the Code 