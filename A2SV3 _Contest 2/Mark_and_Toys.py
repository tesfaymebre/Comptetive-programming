def maximumToys(prices, k):
    prices.sort()
    sum = 0
    for i in range(len(prices)):
        sum += prices[i]
        if sum > k:
            return i
    return len(prices)
