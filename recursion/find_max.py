nums = [2,4,100,6,8,200,10]

# recursively find the maximum number in a list

# def find_max(arr):
#     copied_array = arr
#     max = copied_array[0]
#     if len(copied_array) == 0:
#         return 0
#     elif len(copied_array) == 1:
#         return copied_array[0]
#     else:
#         if max < find_max(copied_array[1:]):
#             max = find_max(copied_array[1:])
#         # print(max)
#         return max

# print(find_max(nums))

# a more efficient way
def sum(arr):
    if len(arr) == 0:
        return 0
    sub_max = sum(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(sum(nums))