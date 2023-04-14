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


def test_drop_first_letter_from_abc() -> None:
    actual_result = drop_first_letter("abc")
    expected_result = "bc"
    assert actual_result == expected_result


def test_drop_first_letter_from_empty_word() -> None:
    actual_result = drop_first_letter("")
    expected_result = ""
    assert actual_result == expected_result


def test_calculate_digit_sum_for_42() -> None:
    actual_result = calculate_digit_sum(42)
    expected_result = 6
    assert actual_result == expected_result


def test_calculate_digit_sum_not_possible_for_negative_num() -> None:
    with pytest.raises(ValueError):
        calculate_digit_sum(-1)
