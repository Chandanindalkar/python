# def countdown(i):
#     print(i)
#     if i <= 1: # base case - case for terminating
#         return
#     else: # recursive case - where the function calls itself with modified arguments to solve a smaller instance of the same problem.
#         countdown(i-1)

# countdown(5)


def countdown(i, result=""):
    result += str(i) + ".." if i > 1 else str(i)  # Append number with ".." or without at the end
    if i <= 1:  # Base case
        print(result)
        return
    else:  # Recursive case
        countdown(i - 1, result)

countdown(5)
