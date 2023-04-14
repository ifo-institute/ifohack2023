def is_even(num: int) -> bool:
    return num % 2 == 0


def drop_first_letter(word: str) -> str:
    return word[1:]


def calculate_digit_sum(num: int) -> int:
    if num < 0:
        raise ValueError('num should be a positive number')
    return sum([int(d) for d in str(num)])
