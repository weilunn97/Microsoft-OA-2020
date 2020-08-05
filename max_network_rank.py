from typing import List


def max_network_rank(A: List[int], B: List[int], N: int) -> int:
    """
    Time  : O(A + B)
    Space : O(N)
    """
    # ADJ[I] = NUMBER OF EDGES ADJACENT TO NODE I
    adj = [0] * (N + 1)

    # FILL UP ADJ - O(A + B)
    for a, b in zip(A, B):
        adj[a] += 1
        adj[b] += 1

    # GET THE MAX NETWORK RANK
    max_rank = 0

    # UPDATE MAX RANK AS WE PROCESS EACH ROAD AGAIN
    for a, b in zip(A, B):
        max_rank = max(max_rank, adj[a] + adj[b] - 1)

    return max_rank


if __name__ == "__main__":
    print(max_network_rank([1, 2, 3, 3], [2, 3, 1, 4], 4) == 4)
