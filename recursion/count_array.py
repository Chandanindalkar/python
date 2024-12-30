nums = [2,4,6,8,10]

# recursively count the list elements

def count_array(arr):
    total = 0
    copied_array = arr
    if len(copied_array) == 0:
        return 0
    else:
        total += 1 + count_array(copied_array[1:])
        # print(total)
        return total

print(count_array(nums))

# a more efficient way
def counter(arr):
    if len(arr) == 0:
        return 0
    return 1 + counter(arr[1:])

print(counter(nums))