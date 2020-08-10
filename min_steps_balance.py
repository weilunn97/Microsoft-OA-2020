from typing import List


def min_steps_balance(piles: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(1), where N = len(s)
    """
    # SORT THE PILE
    piles = sorted(piles, reverse=True)

    # SETUP 2 POINTERS
    i = 0
    steps = 0

    while i < len(piles):
        if piles[i] == piles[-1]:
            return steps
        while i < len(piles) - 1 and piles[i] == piles[i + 1]:
            i += 1
        steps += i + 1
        i += 1
        i = i
    return steps


if __name__ == "__main__":
    print(min_steps_balance([50]) == 0)
    print(min_steps_balance([10, 10]) == 0)
    print(min_steps_balance([5, 5, 5, 2, 2, 1]) == 8)
    print(min_steps_balance([5, 2, 1]) == 3)
    print(min_steps_balance([4, 2, 1]) == 3)
    print(min_steps_balance([4, 5, 5, 4, 2]) == 6)
    print(min_steps_balance([4, 8, 16, 32]) == 6)
    print(min_steps_balance([4, 8, 8]) == 2)
    print(min_steps_balance([4, 4, 8, 8]) == 2)
    print(min_steps_balance([1, 2, 2, 3, 3, 4]) == 9)
    print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)
