nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    i, j, k = 0, 1, len(nums)-1
    while k <= len(nums)-1:
        total = (nums[i] + nums[j] + nums[k])
        if total == 0:
            return [nums.index(i), nums.index(i), nums.index(i)]
        else:

