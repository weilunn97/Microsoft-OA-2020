from typing import List


def cheapest_deletions(s: str, cost: List[int]) -> int:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    # TRACK THE TOTAL DELETION COST THUS FAR
    total_cost = 0

    # PROCESS EACH CHAR
    for i in range(1, len(s)):

        # CHECK FOR DUPLICATE
        if s[i - 1] == s[i]:
            total_cost += min(cost[i - 1], cost[i])

    return total_cost


if __name__ == "__main__":
    print(cheapest_deletions("aaabbb", [3, 2, 1, 3, 2, 1]) == 6)
    print(cheapest_deletions("abccbd", [0, 1, 2, 3, 4, 5]) == 2)
    print(cheapest_deletions("aabbcc", [1, 2, 1, 2, 1, 2]) == 3)
    print(cheapest_deletions("aaaa", [3, 4, 5, 6]) == 12)
    print(cheapest_deletions("ababa", [10, 5, 10, 5, 10]) == 0)
    print(cheapest_deletions("ab", [1, 3]) == 0)
    print(cheapest_deletions("abbb", [1, 3, 2, 1]) == 3)
