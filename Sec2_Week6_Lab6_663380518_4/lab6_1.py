# lab6_1.py

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float):
    """Returns the quotient of two numbers or an error message on division by zero."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(base: float, exponent: float = 2) -> float:
    """Calculates base raised to power. Defaults to exponent=2 (squaring)."""
    return base ** exponent

def main():
    """Interactive menu program for arithmetic operations."""
    while True:
        print("\n--- Simple Calculator Menu ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (Challenge)")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ").strip()
        
        if choice == "6":
            print("Exiting calculator. Goodbye!")
            break
            
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numerical values.")
                continue

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
                
        elif choice == "5":
            try:
                base = float(input("Enter base number: "))
                exp_str = input("Enter exponent (leave blank for default=2): ").strip()
                if exp_str == "":
                    print(f"Result: {power(base)}")
                else:
                    print(f"Result: {power(base, float(exp_str))}")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid choice! Please select an option from 1 to 6.")

if __name__ == "__main__":
    main()