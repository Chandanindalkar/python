nums = [2,4,6,8,10]

def sum_array(arr):
    total = 0
    copied_array = arr
    if len(copied_array) == 0:
        return 0
    elif len(copied_array) == 1:
        return copied_array[0]
    else:
        total += copied_array.pop(0) + sum_array(copied_array)
        # print(total)
        return total

print(sum_array(nums))