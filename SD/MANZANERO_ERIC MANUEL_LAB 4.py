# Simple Modular Calculator

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division (handles division by zero)
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Main program - Menu-driven calculator
def main():
    while True:
        # Display menu
        print("\n📌 Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Exit condition
        if choice == "5":
            print("📕 Exiting calculator. Goodbye!")
            break

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("⚠️ Error: Please enter valid numeric values.")
            continue

        # Perform the selected operation
        if choice == "1":
            print(f"✅ Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"✅ Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"✅ Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"✅ Result: {divide(num1, num2)}")
        else:
            print("⚠️ Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
