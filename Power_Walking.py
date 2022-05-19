from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    powers = list(map(int, input().split()))
    freq = Counter(powers)
    powers.sort(key = lambda x: freq[x])
    count = len(freq)

    for k in range(1,n + 1):
        if k > len(freq):
            count += 1
        
        print(count, end = " ")

    print()