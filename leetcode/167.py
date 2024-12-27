nums = [0, 0, 3, 11]
target = 0


def twoSum(nums, target): # key is element, values is index
    map = {}
    for i, n in enumerate(nums):
        sub = target - n
        if sub in map:
            return [map[sub]+1, i+1]
        map[n] = i


res = twoSum(nums, target)
print(res)
