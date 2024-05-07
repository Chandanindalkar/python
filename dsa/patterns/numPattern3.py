n = 10
# 1
# 11
# 202
# 3003
# 40004
i = 1
while i <= n:
    j = 1
    if i == 1:
        print(1)
        
    elif i == 2:
        print(11)
        
    else: # i is 3 when this loop begins
        while j <= i:
            if j == 1:
                print(i-1, end="")
                j+=1
            elif j > 1 and j < i:
                print(0, end="")
                j+=1
            else:
                print(i-1, end="")
                j+=1
        print()
    i+=1

