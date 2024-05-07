n = 5
#     1
#    121
#   12321
#  1234321
# 123454321
i = 1
while i <= n: # 2
    j = 1
    p = 1
    while j <= (n*2)-1: # 
        if j < n-i+1:
            print(" ", end="")
            j+=1
            
        elif j > n+i-1:
            print(" ", end="")
            j+=1
            
        else:
            if j <= n:
                print(p, end="")
                p+=1
                j+=1
            elif j > n:
                print(p-2, end="")
                p-=1
                j+=1
    print()
    i+=1
