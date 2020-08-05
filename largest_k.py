from typing import List


def largest_k(arr: List[int]) -> int:
    """
    Time  : O(N)
    Space : O(N), where N = len(arr)
    """
    # CONVERT INTO SET, TRACK THE MAXIMUM VALUE OF K
    arr = set(arr)
    max_k = 0

    # TRY EVERY ARRAY ELEMENT
    while arr:
        k = arr.pop()
        max_k = max(max_k, k) if -k in arr else max_k

    return max_k


if __name__ == "__main__":
    print(largest_k([3, 2, -2, 5, -3]) == 3)
    print(largest_k([1, 2, 3, -4]) == 0)
