def reverse(x: int) -> int:
    str_x = str(x)
    rev = int('-' + str_x[::-1][:-1] if x < 0 else str_x[::-1])

    upper_limit = 0x7fffffff
    lower_limit = -0x80000000

    if (rev < 0 and (rev & lower_limit) == lower_limit) or (0 <= rev == (rev & upper_limit)):
        return rev
    return 0
