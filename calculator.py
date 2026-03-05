"""Quick-Calc: Calculator logic module."""


class Calculator:
    """Calculator class containing core calculation logic."""

    def __init__(self):
        self.current_input = "0"
        self.previous_input = None
        self.operator = None

    def clear(self):
        """Reset the calculator to initial state."""
        self.current_input = "0"
        self.previous_input = None
        self.operator = None
        return self.current_input

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide two numbers. Raises ValueError for division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def set_operator(self, operator):
        """Set the current operator."""
        self.operator = operator
        self.previous_input = self.current_input
        self.current_input = "0"

    def input_digit(self, digit):
        """Input a digit to the current number."""
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        return self.current_input

    def calculate(self):
        """Perform the calculation with current operator and inputs."""
        if self.previous_input is None or self.operator is None:
            return self.current_input

        try:
            a = float(self.previous_input)
            b = float(self.current_input)

            if self.operator == "+":
                result = self.add(a, b)
            elif self.operator == "-":
                result = self.subtract(a, b)
            elif self.operator == "*":
                result = self.multiply(a, b)
            elif self.operator == "/":
                result = self.divide(a, b)
            else:
                return self.current_input

            result = int(result) if result == int(result) else result
            self.current_input = str(result)
            self.previous_input = None
            self.operator = None
            return self.current_input

        except ValueError as e:
            if "Cannot divide by zero" in str(e):
                raise e
            return "Error"
