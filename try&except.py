try:
    value = 1
    i = input(print("Enter a number:"))
    print(i)

except ZeroDivisionError as error:
    print(error)

except ValueError:
    print("Invalid Input")