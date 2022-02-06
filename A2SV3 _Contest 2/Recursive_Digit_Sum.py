def superDigit(n, k):
    p = list(map(int,n))
    total = str(sum(p) * k)

    if len(total) == 1:
        return int(total)

    return superDigit(total,1)
