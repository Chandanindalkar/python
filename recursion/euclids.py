x = 640
y = 1680

# doesnt work when y can accomodate more than 2x
def euclid(x, y):
    if y == (2*x):
        print(x)
        return x
    else:
        print(x)
        euclid(y-x, x)

euclid(x,y)