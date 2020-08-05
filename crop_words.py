def crop_words(s: str, k: int) -> str:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    # KEEP A STACK OF ALL THE CHARACTERS THAT MADE IT
    stk = []

    # LOOP TILL LENGTH EXCEEDED
    i = 0
    while i < len(s) and len(stk) < k:
        stk.append(s[i])
        i += 1

    # CHECK IF WE NEED TO POP THE LAST WORD
    while i < len(s) and s[i].isalpha() and stk and stk[-1].isalpha():
        stk.pop()
    return ''.join(stk).rstrip()


if __name__ == "__main__":
    print(crop_words("codility We test coders", 0) == "")
    print(crop_words("codility We test coders", 14) == "codility We")
    print(crop_words(" co de my", 5) == " co")
    print(crop_words(" co de my", 7) == " co de")
    print(crop_words("   ", 1) == "")
    print(crop_words("   ", 2) == "")
    print(crop_words("   re", 2) == "")  # 3
    print(crop_words(" c ", 3) == " c")
    print(crop_words(" c d  ", 5) == " c d")
    print(crop_words("co de my", 5) == "co de")
    print(crop_words("Word", 4) == "Word")
    print(crop_words("codility We test coders", 23) == "codility We test coders")
    print(crop_words("withOutSpaces", 7) == "")
    print(crop_words("withOutSpaces", 14) == "withOutSpaces")
    print(crop_words("", 14) == "")
    print(crop_words("Separatedby hyphens", 14) == "Separatedby")
    print(crop_words("      Codility We test coders     ", 14) == "      Codility")  # 6
    print(crop_words("      Codility We test coders     ", 10) == "")  # 6
