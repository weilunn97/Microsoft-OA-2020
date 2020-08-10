from collections import Counter


def min_swaps(s: str) -> int:
    """
    Time  : O(N^2)
    Space : O(N), where N = len(s)
    """
    counter = Counter(s)
    s = list(s)

    # CHECK FOR ONLY 1 ODD COUNT
    if len([v for v in counter.values() if v == 1]) > 1:
        return -1

    # SETUP FRONT AND BACK POINTERS
    f, b = 0, len(s) - 1
    swaps = 0

    # FOR EACH CHAR
    while f < b:

        # IF IT'S THE LONER CHAR, POSTPONE IT
        if counter.get(s[f]) == 1:
            swaps += 1
            s[f], s[f + 1] = s[f + 1], s[f]
            continue

        # FIND ITS MATCHING CHAR
        for k in range(b, f, -1):
            if s[f] == s[k]:
                break

        # SWAP TO ITS CORRECT POSITION
        for l in range(k, b):
            s[l], s[l + 1] = s[l + 1], s[l]
            swaps += 1

        f += 1
        b -= 1

    return swaps


if __name__ == "__main__":
    print(min_swaps("mamad") == 3)
    print(min_swaps("asflkj") == -1)
    print(min_swaps("aabb") == 2)
    print(min_swaps("ntiin") == 1)
