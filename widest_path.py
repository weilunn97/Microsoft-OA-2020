from typing import List


def widest_path(X: List[int], Y: List[int]) -> int:
    """
    Time  : O(X LOG X)
    Space : O(1), where N = len(X)
    """
    X = sorted(set(X))
    return max([X[i] - X[i - 1] for i in range(1, len(X))])


if __name__ == "__main__":
    print(widest_path([5, 5, 5, 7, 7, 7], [3, 4, 5, 1, 3, 7]) == 2)
    print(widest_path([6, 10, 1, 4, 3], [2, 5, 3, 1, 6]) == 4)
    print(widest_path([4, 1, 5, 4], [4, 5, 1, 3]) == 3)
