from typing import List


def aladdin_checkers(b: List[str]) -> int:
    """
    Time  : O()
    Space : O(1), where S = len(s)
    """
    # CONVERT IT INTO A BOARD
    b = [list(row) for row in b]
    nrows, ncols = len(b), len(b[0])

    # GET JAFFAR'S PAWN POSITION
    jaf = [[i, j] for i in range(nrows) for j in range(ncols) if b[i][j] == "O"][0]

    # START A DFS FROM JAFFAR'S POSITION
    MAX = [0]
    dfs(b, jaf[0], jaf[1], 0, MAX)
    return MAX[0]


def dfs(b: List[List[str]], i: int, j: int, pawns_beaten: int, MAX: List[int]) -> None:
    # BASE CASE - OOB OR I JUMPED INTO ALADDIN'S PAWN
    if min(i, j) < 0 or i >= len(b) or j >= len(b[0]) or b[i][j] == 'X':
        return

    # UPDATE THE MAX
    MAX[0] = max(MAX[0], pawns_beaten)

    # ENSURE WE'RE NOT ON THE TOP EDGE
    if i > 0:
        # TOP-LEFT ATTACK
        if j > 0 and b[i - 1][j - 1] == 'X':
            dfs(b, i - 2, j - 2, pawns_beaten + 1, MAX)

        # TOP-RIGHT ATTACK
        if j < len(b[0]) - 1 and b[i - 1][j + 1] == 'X':
            dfs(b, i - 2, j + 2, pawns_beaten + 1, MAX)


if __name__ == "__main__":
    print(aladdin_checkers(["..X...",
                            "......",
                            "....X.",
                            ".X....",
                            "..X.X.",
                            "...O.."]) == 2)

    print(aladdin_checkers(["X....",
                            ".X...",
                            "..O..",
                            "...X.",
                            "....."]) == 0)
