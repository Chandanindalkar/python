n = 5
#     *
#    **
#   ***
#  ****
# *****
i = 1
while i <= n:
    j = 1
    while j <= n:
        if j < n-i+1:
            print(" ", end="")
            j+=1
        else:
            print("*", end="")
            j+=1

    print()
    i+=1

