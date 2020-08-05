def fill_question_marks(s: str) -> str:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    s = list(s)

    # PROCESS EACH CHAR
    for i in range(len(s)):
        if s[i] == '?':

            # TRY EVERY ALPHABET FROM a - z
            for j in range(26):
                char = chr(ord('a') + j)

                # CHECK LEFT AND RIGHT
                left = i == 0 or s[i - 1] != char
                right = i == len(s) - 1 or s[i + 1] != char
                if left and right:
                    s[i] = char
                    break

    return ''.join(s)


if __name__ == "__main__":
    strings = ["ab?ac?", "rd?e?wg??", "????????"]
    [print(f"{s} --> {fill_question_marks(s)}") for s in strings]
