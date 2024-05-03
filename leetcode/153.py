nums = [4,5,6,7,0,1,2]


def binSearch(nums):
    lo, hi = 0, len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_num = nums[mid]

        if mid > 0 and mid_num < nums[mid-1]:
            return mid_num

        elif mid_num < nums[hi]:
            hi = mid-1
        else:
            lo = mid+1

    return -1

