from typing import List


def day_of_week(day: List[int], k: int) -> str:
    """
    Time  : O(1)
    Space : O(1)
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day_num = {days[i]: i for i in range(len(days))}
    k %= 7
    return days[(day_num.get(day) + k) % len(days)]


if __name__ == "__main__":
    print(day_of_week("Mon", 0) == "Mon")
    print(day_of_week("Mon", 7) == "Mon")
    print(day_of_week("Mon", 8) == "Tue")
    print(day_of_week("Wed", 2) == "Fri")
    print(day_of_week("Sat", 23) == "Mon")
    print(day_of_week("Sun", 1) == "Mon")
    print(day_of_week("Sun", 8) == "Mon")
    print(day_of_week("Sun", 10) == "Wed")
    print(day_of_week("Sun", 70000000000000000000000000000000000000000000000) == "Sun")
