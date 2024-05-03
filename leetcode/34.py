# Find First and Last Position of Element in Sorted Array

test = [
    {'input': {'nums': [5, 7, 7, 8, 8, 10], 'target': 8}, 'output': [3, 4]},
    {'input': {'nums': [1], 'target': 1}, 'output': [0, 0]}
]


def check_start(nums, target, mid):
    mid_num = nums[mid]
    if mid_num == target:
        if mid-1 >= 0 and nums[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_num > target:
        return 'left'
    elif mid_num < target:
        return 'right'


def check_end(nums, target, mid2):
    mid_num2 = nums[mid2]
    if mid_num2 == target:
        if mid2+1 <= len(nums)-1 and nums[mid2+1] == target:
            return 'right'
        else:
            return 'found'
    elif mid_num2 > target:
        return 'left'
    elif mid_num2 < target:
        return 'right'


def find_start(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = (lo+hi) // 2
        result = check_start(nums, target, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1

    return -1


def find_end(nums, target):
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid2 = (lo+hi) // 2
        result2 = check_end(nums, target, mid2)
        if result2 == 'found':
            return mid2
        elif result2 == 'left':
            hi = mid2-1
        elif result2 == 'right':
            lo = mid2+1

    return -1


res1 = find_start(test[1]['input']['nums'], test[1]['input']['target'])
res2 = find_end(test[1]['input']['nums'], test[1]['input']['target'])
print([res1, res2], sep=", ")
