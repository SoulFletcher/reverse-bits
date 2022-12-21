def reverse_bits(n: int) -> int:
    return int(str(format(n, '032b'))[::-1], 2)
