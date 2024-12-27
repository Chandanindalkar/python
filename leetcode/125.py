s = "A man, a plan, a canal: Panama"


def palindrome(s):
    new = s.lower()
    print(new)
    result = ""
    for letter in new:
        if (letter >= "a" and letter <= "z") or ("0" <= letter <= "9"):
            result += letter # learn

    return result


res = palindrome(s)
print(res)