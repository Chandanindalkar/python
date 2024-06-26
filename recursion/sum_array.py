nums = [2,4,6,8,10]

# recursively add list elements

# def sum_array(arr):
#     total = 0
#     copied_array = arr
#     if len(copied_array) == 0:
#         return 0
#     elif len(copied_array) == 1:
#         return copied_array[0]
#     else:
#         total += copied_array.pop(0) + sum_array(copied_array)
#         # print(total)
#         return total

# print(sum_array(nums))

# a more efficient way
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])

print(sum(nums))