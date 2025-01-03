nums = [9,2,5,1,11,4,3]


def insertion_sort(arr, length=1):

    if length == len(arr):
        return arr
    else:
        key = arr[length]
        j = length-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
        return insertion_sort(arr, length=(length+1))


print(insertion_sort(nums))