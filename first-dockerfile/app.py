def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b

def square_root(a):
    """Return the square root of a."""
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return a ** 0.5

if __name__ == "__main__":
    print("Simple Math Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    
    choice = int(input("Enter choice (1-6): "))
    
    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == 1:
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == 2:
            print(f"{a} - {b} = {subtract(a, b)}")
        elif choice == 3:
            print(f"{a} * {b} = {multiply(a, b)}")
        elif choice == 4:
            print(f"{a} / {b} = {divide(a, b)}")
        elif choice == 5:
            print(f"{a} ^ {b} = {power(a, b)}")
    
    elif choice == 6:
        a = float(input("Enter a number: "))
        print(f"Square root of {a} = {square_root(a)}")
    
    else:
        print("Invalid choice")