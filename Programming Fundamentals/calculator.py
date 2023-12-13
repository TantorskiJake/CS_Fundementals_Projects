# Import the math module to use mathematical functions
import math

# Create a Calculator class to perform various mathematical operations
class Calculator:
    def __init__(self):
        self.memory = None  # Initialize memory attribute to store values

    # Basic arithmetic operations
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    # Perform division with exception handling for division by zero
    def divide(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"

    # Exponential function
    def exponentiate(self, x, y):
        return x ** y

    # Square root function
    def square_root(self, x):
        return math.sqrt(x)

    # Trigonometric functions, converting degrees to radians
    def sine(self, x):
        return math.sin(math.radians(x))

    def cosine(self, x):
        return math.cos(math.radians(x))

    def tangent(self, x):
        return math.tan(math.radians(x))

    # Logarithmic function with input validation
    def logarithm(self, x, base):
        if x > 0 and base > 1:
            return math.log(x, base)
        else:
            return "Invalid input for logarithm"

    # Store a value in memory
    def store_in_memory(self, value):
        self.memory = value

    # Recall the value stored in memory
    def recall_memory(self):
        return self.memory if self.memory is not None else "Memory is empty"

# Create an instance of the Calculator class
calculator = Calculator()

# Dictionary to map user input to corresponding calculator operations
operations = {
    '1': calculator.add,
    '2': calculator.subtract,
    '3': calculator.multiply,
    '4': calculator.divide,
    '5': calculator.exponentiate,
    '6': calculator.square_root,
    '7': calculator.sine,
    '8': calculator.cosine,
    '9': calculator.tangent,
    '10': calculator.logarithm
}

# Function to get numeric input from the user with exception handling
def get_user_input():
    while True:
        try:
            return float(input("Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Function to display the result with appropriate formatting
def display_result(result):
    print(f"Result: {result:.6f}" if isinstance(
        result, float) else f"Result: {result}")

# Main loop for user interaction
while True:
    # Display available operations to the user
    print("\nSelect operation:")
    for key, value in operations.items():
        print(f"{key}. {value.__name__.capitalize()}")

    # Additional options for storing and recalling values in memory, and exiting the calculator
    print("11. Store in Memory")
    print("12. Recall Memory")
    print("13. Exit")

    # Get user choice
    choice = input("Enter choice (1-13 or 'exit'): ")

    # Check user choice and perform the corresponding operation
    if choice.lower() in ('13', 'exit'):
        print("Exiting the calculator. Goodbye!")
        break

    if choice in operations:
        num1 = get_user_input()

        # Special handling for square root and trigonometric functions that take a single input
        if choice in ('6', '7', '8', '9'):
            result = operations[choice](num1)
        else:
            num2 = get_user_input()
            result = operations[choice](num1, num2)

        # Display the result to the user
        display_result(result)
    elif choice == '11':
        # Store a value in memory with input validation
        try:
            value_to_store = float(input("Enter value to store in memory: "))
            calculator.store_in_memory(value_to_store)
            print("Value stored in memory.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif choice == '12':
        # Recall the value from memory and display it to the user
        recalled_value = calculator.recall_memory()
        print("Recalled value from memory:", recalled_value)
    else:
        print("Invalid choice. Please enter a number between 1 and 13.")
