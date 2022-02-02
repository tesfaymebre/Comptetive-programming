def twoStacks(maxSum, a, b):
    moves = 0
    total = 0
    stack = []

    for x in a:
        if (total + x) > maxSum:
            break

        stack.append(x)
        moves += 1
        total += x

    maxScore = moves

    for y in b:
        total += y
        moves += 1

        while total > maxSum and stack:
            total -= stack.pop()
            moves -= 1

        if total <= maxSum and moves > maxScore:
            maxScore = moves

    return maxScore
