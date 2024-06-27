def countdown(i):
    print(i)
    if i <= 1: # base case - case for terminating
        return
    else: # recursive case - where the function calls itself with modified arguments to solve a smaller instance of the same problem.
        countdown(i-1)

countdown(5)