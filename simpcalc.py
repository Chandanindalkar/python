def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y

x = int(input("Enter the first operand:"))
y = int(input("Enter the second operand:"))
print("Select Operation to be performed")
choice = int(input("1.Add\n 2.Sub\n 3.Mul\n 4.Div\n"))

if choice == 1:
    print(x, "+", y, "=", add(x, y))

elif choice == 2:
    print(x, "-", y, "=", sub(x, y))

elif choice == 3:
    print(x, "*", y, "=", mul(x, y))

elif choice == 4:
    print(x, "/", y, "=", div(x, y))

else:
    print("Invalid Input")
