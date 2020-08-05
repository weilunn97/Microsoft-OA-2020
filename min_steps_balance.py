from typing import List


def min_steps_balance(piles: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(1), where N = len(s)
    """

    # EDGE CASE
    if len(piles) < 2:
        return 0

    # SORT THE BLOCKS
    piles = sorted(piles, reverse=True)

    # COUNT THE STEPS WE NEED
    steps = 0

    # EACH TIME WE SEE A DIFFERENT ELEMENT, WE NEED TO SEE HOW MANY ELEMENTS ARE BEFORE IT
    for i in range(1, len(piles)):
        steps += i if piles[i - 1] != piles[i] else 0

    return steps


if __name__ == "__main__":
    print(min_steps_balance([50]) == 0)
    print(min_steps_balance([10, 10]) == 0)
    print(min_steps_balance([5, 2, 1]) == 3)
    print(min_steps_balance([4, 2, 1]) == 3)
    print(min_steps_balance([4, 5, 5, 4, 2]) == 6)
    print(min_steps_balance([4, 8, 16, 32]) == 6)
    print(min_steps_balance([4, 8, 8]) == 2)
    print(min_steps_balance([4, 4, 8, 8]) == 2)
    print(min_steps_balance([1, 2, 2, 3, 3, 4]) == 9)
    print(min_steps_balance([1, 1, 2, 2, 2, 3, 3, 3, 4, 4]) == 15)
