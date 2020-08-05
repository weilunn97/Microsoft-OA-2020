def longest_sub(s: str) -> str:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    front, back = 0, 0
    a, b = 0, 0
    longest = ""

    # LOOP TILL BACK OOB
    while back < len(s):

        # ADD THE BACK CHAR
        if s[back] == 'a':
            a += 1
            b = 0

        else:
            b += 1
            a = 0

        # TEST FOR VIOLATION (>=3 ADJACENT CHARS)
        if max(a, b) == 3:
            longest = s[front: back] if back - front > len(longest) else longest
            front = back
            a, b = 0, 0
            continue

        back += 1

    # FINAL UPDATE
    if max(a, b) < 3:
        longest = s[front: back] if back - front > len(longest) else longest

    return longest


if __name__ == "__main__":
    print(longest_sub("aabbaaaaabb") == "aabbaa")
    print(longest_sub("aabbaabbaabbaa") == "aabbaabbaabbaa")
    print(longest_sub("abbaabbaaabbaaa") == "abbaabbaa")
    print(longest_sub("aaaabab") == "aabab")
    print(longest_sub("ababbbb") == "ababb")
    print(longest_sub("ababbbbabababbb") == "bbabababb")
