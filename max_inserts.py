def max_inserts(s: str) -> int:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """

    # CONVERT ALL TO LOWERCASE
    s = s.lower()

    # EDGE CASE
    if "aaa" in s:
        return -1

    # COUNT THE NUMBER OF CONSECUTIVE 'a' WE'VE SEEN IMMEDIATELY BEFORE US
    count = 0

    # COUNT THE INSERTIONS PERFORMED
    inserts = 0

    # PROCESS EACH CHAR
    for char in s:

        # CASE 1 - AN 'A' - DO NOT PERFORM INSERTION
        if char == 'a':
            count += 1

        # CASE 2 - NOT AN 'A'
        # DEPENDING ON THE NUMBER OF 'a' WE'VE SEEN BEFORE US, WE INSERT MORE 'a'
        else:
            inserts += 2 - count
            count = 0

    # FINAL INSERT
    inserts += 2 - count
    return inserts


if __name__ == "__main__":
    print(max_inserts("aa") == 0)
    print(max_inserts("aaba") == 1)
    print(max_inserts("aabab") == 3)
    print(max_inserts("abaac") == 3)
    print(max_inserts("abab") == 4)
    print(max_inserts("baaaa") == -1)
    print(max_inserts("dog") == 8)
    print(max_inserts("xaxaax") == 5)
