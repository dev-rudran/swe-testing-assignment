# Quick-Calc

A simple calculator application with Tkinter GUI, built as part of the Advanced Software Engineering course. Quick-Calc provides basic arithmetic operations including addition, subtraction, multiplication, division, and clear functionality.

## Features

- **Addition**: Add two numbers (e.g., 5 + 3 = 8)
- **Subtraction**: Subtract two numbers (e.g., 10 - 4 = 6)
- **Multiplication**: Multiply two numbers (e.g., 6 × 7 = 42)
- **Division**: Divide two numbers with division by zero handling (e.g., 20 / 4 = 5)
- **Clear (C)**: Reset the calculator to initial state

## Setup Instructions

### Prerequisites

- Python 3.x
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

To launch the calculator GUI:
```bash
python gui.py
```

## How to Run Tests

This project uses **pytest** as the testing framework.

Run all tests:
```bash
pytest tests/ -v
```

Run only unit tests:
```bash
pytest tests/test_unit.py -v
```

Run only integration tests:
```bash
pytest tests/test_integration.py -v
```

## Testing Framework Research

### Comparison: pytest vs unittest

For Python testing, two popular frameworks are **pytest** and **unittest**. Below is a comparative analysis:

#### unittest
- Built-in Python standard library (no installation required)
- Uses a class-based approach with TestCase classes
- Requires more boilerplate code for test setup and assertions
- Follows xUnit style (similar to JUnit, NUnit)

#### pytest
- Third-party library requiring installation
- Simpler, function-based test design
- Powerful fixture system for test setup/teardown
- Rich plugin ecosystem (pytest-django, pytest-cov, etc.)
- More readable and concise test code
- Automatic test discovery

#### Justification for Choosing pytest

I chose **pytest** for this project because:
1. **Concise syntax**: Tests are simpler and more readable with pytest's function-based approach
2. **Fixture support**: The `@pytest.fixture` decorator provides clean test setup
3. **Better error messages**: pytest shows detailed failure information
4. **Industry adoption**: Widely used in Python projects, making it a valuable skill
5. **Easy to extend**: Plugins like pytest-cov for coverage reporting

While unittest is sufficient for basic testing, pytest's modern approach and extensive features make it more suitable for professional development workflows.
