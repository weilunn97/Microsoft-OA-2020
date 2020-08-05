def min_moves(s: str) -> int:
    # SETUP A COUNT OF A'S AND B'S
    a, b = 0, 0
    replacements = 0

    for char in s:
        if char == 'a':
            while b >= 3:
                replacements += 1
                b -= 3
            a += 1
            b = 0
        else:
            while a >= 3:
                replacements += 1
            b += 1
            a = 0

    while a >= 3:
        replacements += 1
        a -= 3
    while b >= 3:
        replacements += 1
        b -= 3
    return replacements


if __name__ == "__main__":
    print(min_moves("baaa") == 1)
    print(min_moves("baaaa") == 1)
    print(min_moves("baaaaa") == 1)
    print(min_moves("baaaaaa") == 2)
    print(min_moves("baaabbaabbba") == 2)
    print(min_moves("baabab") == 0)
