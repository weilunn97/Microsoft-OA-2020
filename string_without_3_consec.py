def string_without_3_consec(s: str) -> str:
    """
    Time  : O(N)
    Space : O(N), where N = len(s)
    """
    # EDGE CASE
    if len(s) < 3:
        return s

    # SETUP THE FINAL STRING, CURRENT CHAR, AND ITS COUNT
    final = []
    char, count = None, 0

    # PROCESS EACH CHAR
    for c in s:

        # CASE 1 - CHAR MATCHES
        if c == char:
            if count < 2:
                final.append(char)
                count += 1

        # CASE 2 - CHAR DIFFERS
        else:
            char, count = c, 1
            final.append(char)

    return ''.join(final)


if __name__ == "__main__":
    print(string_without_3_consec("eedaaad") == "eedaad")
    print(string_without_3_consec("xxxtxxx") == "xxtxx")
    print(string_without_3_consec("uuuuxaaaaxuuu") == "uuxaaxuu")
