prices = [7, 1, 5, 3, 6, 4]


def toTheMoon(prices):
    profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j]-prices[i]>profit:
                profit = prices[j] - prices[i]
    return profit


res = toTheMoon(prices)
print(res)
