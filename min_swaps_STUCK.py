from collections import Counter


def min_swaps(s: str) -> int:
    """
    Time  : O(N^2)
    Space : O(N), where N = len(s)
    """
    if not is_valid_palindrome(s):
        return -1

    # CONVERT TO LIST
    s = list(s)

    # SETUP FRONT BACK POINTER
    f, b = 0, len(s) - 1
    swaps = 0

    # LOOP TILL CROSS
    while f < b:

        # CASE 1 - THEY'RE EQUAL
        if s[f] == s[b]:
            f += 1
            b -= 1

        # CASE 2 - THEY'RE DIFFERENT
        else:

            # FIND THE RIGHTMOST CHAR TO MATCH FRONT CHAR
            mid = b
            while mid > f and s[f] != s[mid]:
                mid -= 1

            # CASE 1 - CHAR NOT FOUND - SWAP ONCE WITH RIGHT NEIGHBOUR
            if mid == f:
                s[mid], s[mid + 1] = s[mid + 1], s[mid]
                swaps += 1
                continue

            # CASE 2 - CHAR FOUND - SWAP WITH RIGHT NEIGHBOUR UNTIL WE HIT BACK POINTER
            for i in range(mid, b):
                s[i], s[i + 1] = s[i + 1], s[i]
                swaps += 1

            # CLOSE THE WINDOW
            f += 1
            b -= 1

    return swaps


def is_valid_palindrome(s: str) -> bool:
    count = Counter(s)
    return len([char for char, freq in count.items() if freq % 2]) <= 1


if __name__ == "__main__":
    print(min_swaps("mamad") == 3)
    print(min_swaps("asflkj") == -1)
    print(min_swaps("aabb") == 2)
    print(min_swaps("ntiin") == 1)
