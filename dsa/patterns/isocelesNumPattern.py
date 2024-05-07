n = 8
#       1
#      232
#     34543
#    4567654
#   567898765
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
                print(p+i-1, end="")
                p+=1
                j+=1
            elif j > n:
                print(p+i-3, end="")
                p-=1
                j+=1
    print()
    i+=1
