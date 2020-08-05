def longest_semi_alt_sub(s: str) -> str:
    """
    Time  : O(N)
    Space : O(N), where N = len(s)
    """
    # EDGE CASE
    if len(s) < 3:
        return s

    # SETUP A SLIDING WINDOW
    front, back = 0, 0
    char, count = None, 0
    longest = 0

    # LOOP TILL BACK OOB
    while back < len(s):

        # CASE 1 - SAME CHAR
        if s[back] == char:

            # HANDLE VIOLATION --> UPDATE LONGEST, RESET WINDOW, AND RESET COUNT
            if count == 2:
                longest = max(longest, back - front)
                front = back - 1
            else:
                count += 1

        # CASE 2 - DIFF CHAR
        else:
            char, count = s[back], 1

        # OPEN THE WINDOW AS USUAL
        back += 1

    # FINAL UPDATE
    longest = max(longest, back - front)

    return longest


if __name__ == "__main__":
    print(longest_semi_alt_sub("baaabbabbbb") == 7)  # aabbabb
    print(longest_semi_alt_sub("babba") == 5)  # babba
    print(longest_semi_alt_sub("abaaaa") == 4)  # abaa
    print(longest_semi_alt_sub("aaabaax") == 6)  # aabaax
    print(longest_semi_alt_sub("aaabaaxx") == 7)  # aabaaxx
    print(longest_semi_alt_sub("aaabaaxxx") == 7)  # aabaaxx
