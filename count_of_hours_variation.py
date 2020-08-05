def count_of_hours_variation(a: int, b: int, c: int, d: int) -> int:
    """
    Time  : O(S)
    Space : O(1), where S = len(s)
    """
    # TRY EACH POSSIBLE COMBINATION
    times = []
    backtrack([a, b, c, d], "", times)
    return len([t for t in set(times) if is_valid(t)])


def backtrack(nums, time, times):
    if not nums:
        times.append(time)
        return

    for i in range(len(nums)):
        popped = nums.pop(i)
        backtrack(nums, f"{time}{popped}", times)
        nums.insert(i, popped)


def is_valid(t):
    hours, mins = t[:2], t[2:]
    return 0 <= int(hours) <= 23 and 0 <= int(mins) <= 59


if __name__ == "__main__":
    print(count_of_hours_variation(1, 0, 0, 2) == 12)
    print(count_of_hours_variation(2, 1, 2, 1) == 6)
    print(count_of_hours_variation(1, 4, 8, 2) == 5)
    print(count_of_hours_variation(4, 4, 4, 4) == 0)
    print(count_of_hours_variation(2, 4, 2, 4) == 1)
    print(count_of_hours_variation(2, 3, 2, 4) == 4)
