s = "ADOBECODEBANC"
t = "ABC"


def minWindow(s, t):
    l, r = 0, 0
    temp = ''
    result = ''
    while l < len(s):
        temp = (r-l+1)
        print(temp)
        for r in range(len(s)):
            if