s = "pwwkew"


def substring(s):
    if len(s) == 0:
        return 0
    output = 1
    for i in range(len(s)-1):
        temp = s[i]
        j = i+1
        while s[j] not in temp and j < len(s)-1:
            temp += s[j]
            j += 1
        if len(temp) > output:
            output = len(temp)
    return output


res = substring(s)
print(res)