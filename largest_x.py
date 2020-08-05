from collections import Counter
from typing import List


def largest_x(arr: List[int]) -> int:
    """
    Time  : O(N)
    Space : O(1), where N = len(arr)
    """
    # GET A COUNT OF ALL NUMBERS
    counter = Counter(arr)

    # GET THE MAXIMUM NUMBER
    max_num = 0

    for num, freq in counter.items():
        if num == freq and freq >= max_num:
            max_num = num
    return max_num


if __name__ == "__main__":
    print(largest_x([3, 8, 2, 3, 3, 2]) == 3)
    print(largest_x([7, 1, 2, 8, 2]) == 2)
    print(largest_x([3, 1, 4, 1, 5]) == 0)
    print(largest_x([5, 5, 5, 5, 5]) == 5)
