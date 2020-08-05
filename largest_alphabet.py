def largest_alphabet(s: str) -> int:
    """
    Time  : O(S)
    Space : O(1), where S = len(s)
    """
    largest = None
    s = set(s)

    for char in s:
        if char.isupper() and char.lower() in s:
            largest = char if largest is None or char > largest else largest

    return largest or "NO"


if __name__ == "__main__":
    print(largest_alphabet("admeDCAB") == "D")
    print(largest_alphabet("adZybxYx") == "Y")
    print(largest_alphabet("AdmeDCAB") == "D")
    print(largest_alphabet("abc") == "NO")
