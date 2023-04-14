import pytest
from .main import is_even, drop_first_letter, calculate_digit_sum


def test_is_even_is_true_for_even_number() -> None:
    actual_result = is_even(2)
    expected_result = True
    assert actual_result == expected_result


def test_is_even_is_false_for_odd_number() -> None:
    actual_result = is_even(1)
    expected_result = False
    assert actual_result == expected_result

# please add further tests here
