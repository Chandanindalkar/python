test = [
    {'input': {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'target': 4}, 'output': 6},
    {'input': {'cards': [], 'target': 3}, 'output': -1},
    {'input': {'cards': [10, 9, 9, 8, 8, 7, 7, 5, 4, 3], 'target': 8}, 'output': 3},
]


def check_location(cards, target, mid):
    mid_card = cards[mid]
    if mid_card == target:
        # this check if the previous element from the found target is also the target
        # In that case the first occurring element is to be returned
        if mid-1 >= 0 and cards[mid-1] == target:
            return 'left'
        else:
            return 'found'
    elif mid_card > target:
        return 'right'
    elif mid_card < target:
        return 'left'


def find_card(cards, target):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        result = check_location(cards, target, mid)
        if result == 'found':
            return mid
        elif result == 'right':
            lo = mid+1
        elif result == 'left':
            hi = mid-1

    return -1


res = find_card(test[2]['input']['cards'], test[2]['input']['target'])
print(res)
