nums = [14, 7, 4, 12, 9, 11, 3, 6, 2]


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])

    result = merger(left, right)
    return result


def merger(left, right):
    # merges two sorted arrays to produce one sorted array
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            left.pop(0)
        else:
            result.append(right[j])
            right.pop(0)

    if len(left) > 0:
        result = result + left

    if len(right) > 0:
        result = result + right

    return result


print(mergeSort(nums))
