"""Unit tests for Calculator class."""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Create a Calculator instance for testing."""
    return Calculator()


class TestAddition:
    """Tests for addition operation."""

    def test_add_positive_numbers(self, calc):
        assert calc.add(5, 3) == 8

    def test_add_negative_numbers(self, calc):
        assert calc.add(-5, -3) == -8

    def test_add_mixed_numbers(self, calc):
        assert calc.add(-5, 10) == 5


class TestSubtraction:
    """Tests for subtraction operation."""

    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_subtract_result_negative(self, calc):
        assert calc.subtract(3, 7) == -4


class TestMultiplication:
    """Tests for multiplication operation."""

    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(6, 7) == 42

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0


class TestDivision:
    """Tests for division operation."""

    def test_divide_positive_numbers(self, calc):
        assert calc.divide(20, 4) == 5

    def test_divide_result_with_decimal(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero_raises_error(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)


class TestEdgeCases:
    """Tests for edge cases."""

    def test_clear_resets_calculator(self, calc):
        calc.input_digit("5")
        calc.set_operator("+")
        calc.input_digit("3")
        result = calc.clear()
        assert result == "0"
        assert calc.previous_input is None
        assert calc.operator is None

    def test_large_numbers(self, calc):
        result = calc.multiply(1000000, 1000000)
        assert result == 1000000000000

    def test_decimal_numbers(self, calc):
        result = calc.add(1.5, 2.5)
        assert result == 4.0
