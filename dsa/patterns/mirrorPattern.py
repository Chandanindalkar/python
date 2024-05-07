n = 5
#     1
#    12
#   123
#  1234
# 12345

i = 1
while i <= n:
    j = 1
    p = 1
    while j <= n:
        if j < n-i+1:
            print(" ", end="")
            j+=1
        
        else:
            print(p, end="")
            j+=1
            p+=1

    print()
    i+=1

