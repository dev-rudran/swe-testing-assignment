"""Integration tests for Calculator - full user workflows."""

import pytest
from calculator import Calculator


class TestIntegration:
    """Integration tests for full user workflows."""

    def test_full_addition_workflow(self):
        """Test complete addition: 5 + 3 = 8"""
        calc = Calculator()
        calc.input_digit("5")
        calc.set_operator("+")
        calc.input_digit("3")
        result = calc.calculate()
        assert result == "8"

    def test_full_subtraction_workflow(self):
        """Test complete subtraction: 10 - 4 = 6"""
        calc = Calculator()
        calc.input_digit("1")
        calc.input_digit("0")
        calc.set_operator("-")
        calc.input_digit("4")
        result = calc.calculate()
        assert result == "6"

    def test_full_multiplication_workflow(self):
        """Test complete multiplication: 6 * 7 = 42"""
        calc = Calculator()
        calc.input_digit("6")
        calc.set_operator("*")
        calc.input_digit("7")
        result = calc.calculate()
        assert result == "42"

    def test_full_division_workflow(self):
        """Test complete division: 20 / 4 = 5"""
        calc = Calculator()
        calc.input_digit("2")
        calc.input_digit("0")
        calc.set_operator("/")
        calc.input_digit("4")
        result = calc.calculate()
        assert result == "5"

    def test_clear_after_calculation(self):
        """Test that Clear resets display to 0 after calculation."""
        calc = Calculator()
        calc.input_digit("5")
        calc.set_operator("+")
        calc.input_digit("3")
        calc.calculate()
        result = calc.clear()
        assert result == "0"

    def test_chained_operations(self):
        """Test multiple operations in sequence."""
        calc = Calculator()
        calc.input_digit("5")
        calc.set_operator("+")
        calc.input_digit("3")
        calc.calculate()
        calc.set_operator("*")
        calc.input_digit("2")
        result = calc.calculate()
        assert result == "16"

    def test_decimal_calculation(self):
        """Test calculation with decimal numbers."""
        calc = Calculator()
        calc.input_digit("1")
        calc.input_digit(".")
        calc.input_digit("5")
        calc.set_operator("+")
        calc.input_digit("2")
        calc.input_digit(".")
        calc.input_digit("5")
        result = calc.calculate()
        assert result == "4"
