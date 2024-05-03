
test = [
    {'input': {'cards': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 'target': 7}, 'output': 3},
    {'input': {'cards': [], 'target': 3}, 'output': -1},
]


def find_card(cards, target):
    position = 0

    while position < len(cards):

        if cards[position] == target:
            return position

        position += 1

    return -1


# change test[index] to run other cases in test list
result = find_card(test[1]['input']['cards'], test[1]['input']['target'])
print(result)
