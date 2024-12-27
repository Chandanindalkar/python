testCase = [
    {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'target': 4},
    {'cards': [], 'target': 3},
    {'cards': [10, 9, 9, 8, 8, 7, 7, 5, 4, 3], 'target': 8},
]


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
    
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            low = mid+1
        elif arr[mid] < target:
            high = mid-1
    return -1


res = binary_search(testCase[0]['cards'], testCase[0]['target'])
print(res)