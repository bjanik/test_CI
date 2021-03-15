
def reverse_digits(n: int) -> int:
    s = str(n) if n >= 0 else str(n)[1:]
    return int(s[::-1]) if n >= 0 else int(s[::-1]) * -1
