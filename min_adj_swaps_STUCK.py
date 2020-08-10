from collections import Counter


def min_adj_swaps(s: str) -> int:
    """
    Time  : O()
    Space : O(), where N = len(s)
    """


if __name__ == "__main__":
    print(min_adj_swaps("WRRWWR") == 2)
    print(min_adj_swaps("WWRWWWRWR") == 2)
    print(min_adj_swaps("WWW") == 2)
    print(min_adj_swaps("RW" * 100000) == -1)
    print(min_adj_swaps("RRR") == 0)
    print(min_adj_swaps("RRRWWWRR") == 6)
