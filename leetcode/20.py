s = "()[]{}"


def validParenthesis(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            if s[i+1] == ')':
                stack += i
        elif s[i] == '[':
            stack += i
        elif i == '{':
            stack += i
        elif i == ')' or i == ']' or i == '}':
            stack.pop()
    print(stack)
    if len(stack) == 0:
        return True
    else:
        return False


res = validParenthesis(s)
print(res)