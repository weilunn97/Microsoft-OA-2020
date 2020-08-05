from typing import List


def fair_indexes(A: List[int], B: List[int]) -> int:
    """
    Time  : O(A + B)
    Space : O(1), where A = len(A) and B = len(B)
    """

    # GET A PREFIX SUM OF EACH ARRAY
    for i in range(1, len(A)):
        A[i] += A[i - 1]
        B[i] += B[i - 1]

    # TRY EACH INDEX
    fair = 0
    for k in range(1, len(A)):
        left_A, right_A = A[k - 1], A[-1] - A[k - 1]
        left_B, right_B = B[k - 1], B[-1] - B[k - 1]
        fair += int(left_A == right_A == left_B == right_B)

    return fair


if __name__ == "__main__":
    print(fair_indexes([4, -1, 0, 3], [-2, 5, 0, 3]) == 2)
    print(fair_indexes([4, -1, 0, 3], [-2, 6, 0, 4]) == 0)
    print(fair_indexes([3, 2, 6], [4, 1, 6]) == 0)
    print(fair_indexes([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]) == 2)
    print(fair_indexes([2, -2, -3, 3], [0, 0, 4, -4]) == 1)
