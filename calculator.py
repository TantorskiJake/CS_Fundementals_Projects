# Import the math module for mathematical operations
import math

# Define a Calculator class to encapsulate calculator functionalities


class Calculator:
    # Initialize the calculator with a memory variable set to None
    def __init__(self):
        self.memory = None

    # Define method for addition operation
    def add(self, x, y):
        return x + y

    # Define method for subtraction operation
    def subtract(self, x, y):
        return x - y

    # Define method for multiplication operation
    def multiply(self, x, y):
        return x * y

    # Define method for division operation with error handling
    def divide(self, x, y):
        try:
            result = x / y
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"

    # Define method for exponentiation operation
    def exponentiate(self, x, y):
        return x ** y

    # Define method for square root operation
    def square_root(self, x):
        return math.sqrt(x)

    # Define method for sine operation
    def sine(self, x):
        return math.sin(math.radians(x))

    # Define method for cosine operation
    def cosine(self, x):
        return math.cos(math.radians(x))

    # Define method for tangent operation
    def tangent(self, x):
        return math.tan(math.radians(x))

    # Define method for logarithmic operation with input validation
    def logarithm(self, x, base):
        if x > 0 and base > 1:
            return math.log(x, base)
        else:
            return "Invalid input for logarithm"

    # Define method for storing a value in memory
    def store_in_memory(self, value):
        self.memory = value

    # Define method for recalling the value from memory with handling for empty memory
    def recall_memory(self):
        return self.memory if self.memory is not None else "Memory is empty"


# Create an instance of the Calculator class
calculator = Calculator()

# Mapping choices to corresponding functions
operations = {
    '1': calculator.add,        # Addition
    '2': calculator.subtract,   # Subtraction
    '3': calculator.multiply,   # Multiplication
    '4': calculator.divide,     # Division
    '5': calculator.exponentiate,  # Exponentiation
    '6': calculator.square_root,   # Square Root
    '7': calculator.sine,       # Sine function
    '8': calculator.cosine,     # Cosine function
    '9': calculator.tangent,    # Tangent function
    '10': calculator.logarithm  # Logarithmic function
}

# Define a function to get user input for numbers


def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number (if applicable): "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Define a function to display the result


def display_result(result):
    # Use f-string for a more formatted and visually appealing result display
    print(f"Result: {result:.6f}" if isinstance(
        result, float) else f"Result: {result}")


# Main program loop
while True:
    print("\nSelect operation:")
    # Print the available operations and their corresponding numbers
    for key, value in operations.items():
        print(f"{key}. {value.__name__.capitalize()}")

    # Print additional options for storing and recalling memory
    print("11. Store in Memory")
    print("12. Recall Memory")
    print("13. Exit")

    # Get user input for the selected operation
    choice = input("Enter choice (1-13 or 'exit'): ")

    # Check if the user chose to exit
    if choice.lower() in ('13', 'exit'):
        print("Exiting the calculator. Goodbye!")
        break

    # Check if the user choice is a valid operation
    if choice in operations:
        num1, num2 = get_user_input()
        # Execute the selected operation and display the result
        result = operations[choice](num1, num2) if choice in (
            '1', '2', '3', '4', '5', '6') else operations[choice](num1)
        display_result(result)

    # Check if the user choice is to store a value in memory
    elif choice == '11':
        value_to_store = float(input("Enter value to store in memory: "))
        calculator.store_in_memory(value_to_store)
        print("Value stored in memory.")

    # Check if the user choice is to recall a value from memory
    elif choice == '12':
        recalled_value = calculator.recall_memory()
        print("Recalled value from memory:", recalled_value)

    # Handle invalid choices
    else:
        print("Invalid choice. Please enter a number between 1 and 13.")
