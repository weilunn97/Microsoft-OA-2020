from collections import Counter
from math import gcd, factorial
from typing import List, Tuple


def fractions_pair_sum(X: List[int], Y: List[int]) -> int:
    """
    Time  : O()
    Space : O(1), where S = len(s)
    """
    fractions = [simplify(x, y) for x, y in zip(X, Y)]
    counter = Counter(fractions)
    fractions = sorted(set(fractions), key=lambda k: k[0] / k[1])
    front, back = 0, len(fractions) - 1
    count = 0

    while front < back:
        compare = find_frac(fractions[front], fractions[back])
        if compare == -1:
            front += 1
        elif compare == 1:
            back -= 1
        else:
            count += counter[fractions[front]] * counter[fractions[back]]
            front += 1

    # ADD ON ALL SELF-COUNTS
    for frac in counter.keys():
        count += get_self_count(frac, counter)
    return count % (10 ** 9 + 7)


def find_frac(front: Tuple[int, int], back: Tuple[int, int]) -> int:
    n1, d1 = front[0], front[1]
    n2, d2 = back[0], back[1]
    lcm = get_lcm(d1, d2)
    n1 *= int(lcm / d1)
    n2 *= int(lcm / d2)
    top_sum = n1 + n2
    return 1 if top_sum > lcm else -1 if top_sum < lcm else 0


def get_lcm(x: int, y: int) -> int:
    xi, yi = x, y
    while x != y:
        if x < y:
            x += xi
        else:
            y += yi
    return x


def simplify(x: int, y: int) -> (int, int):
    _gcd = gcd(x, y)
    return x // _gcd, y // _gcd


def get_self_count(frac: Tuple[int], counter: dict):
    copies = frac[1] / frac[0]
    if int(copies) == copies and counter[frac] >= copies:
        return choose(counter[frac], copies)
    return 0


def choose(x: int, y: int) -> int:
    return factorial(x) / (factorial(y) * factorial(x - y))


if __name__ == "__main__":
    print(fractions_pair_sum([1, 1, 2], [3, 2, 3]) == 1)
    print(fractions_pair_sum([1, 1, 1], [2, 2, 2]) == 3)
    print(fractions_pair_sum([1, 2, 3, 1, 2, 12, 8, 4], [5, 10, 15, 2, 4, 15, 10, 5]) == 10)
    print(fractions_pair_sum([5, 6, 5], [11, 11, 11]) == 2)
