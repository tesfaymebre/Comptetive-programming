t = int(input())

for i in range(t):
    n = int(input())
    sequences = list(map(int,input().split()))
    sequences.sort()
    red_tot = 0
    blue_tot = sequences[0]

    for j in range(1, n//2 + 1):
        blue_tot += sequences[j]
        red_tot += sequences[-j]
        
        if red_tot > blue_tot:
            print("YES")
            break
    if red_tot <= blue_tot:
        print("NO")
