import pytest

from app.operations import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(10, 4) == 6


def test_multiply() -> None:
    assert multiply(6, 7) == 42


def test_divide() -> None:
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_value_error() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
