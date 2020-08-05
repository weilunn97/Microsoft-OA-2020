from collections import defaultdict
from typing import List


def max_chunks_sorted(arr: List[int]) -> int:
    """
    Time  : O(N log N)
    Space : O(1), where N = len(arr)
    """
    X, Y = defaultdict(int), defaultdict(int)
    chunks = 0

    for x, y in zip(arr, sorted(arr)):
        X[x] += 1
        Y[y] += 1
        chunks += X == Y

    return chunks


if __name__ == "__main__":
    print(max_chunks_sorted([2, 4, 1, 6, 5, 9, 7]) == 3)
    print(max_chunks_sorted([4, 3, 2, 6, 1]) == 1)
    print(max_chunks_sorted([2, 1, 6, 4, 3, 7]) == 3)
