n =  4

# for i in range(1, n+1):
#     for j in range(i, 0, -1):
#         print(j, end='')
#     print()

# k = 3

def getChar(k):
    x = ord('A')
    targetAscii = x+k-1
    targetChar = chr(targetAscii)
    return targetChar

i = 1
while i <= n:
    j = i
    while j <= n+i-1:
        print(getChar(j), end='')
        j+=1
    print()
    i+=1