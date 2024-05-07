nums = [5, 3, 6, 2, 3, 10]


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    # print(smallest)
    return smallest_index


# find_smallest(nums)


def selection_sort(arr):
    new_array = []
    copied_array = arr
    for i in range(len(copied_array)):
        smallest = find_smallest(copied_array)
        new_array.append(copied_array[smallest])
        copied_array.pop(smallest)
    print(new_array)


selection_sort(nums)