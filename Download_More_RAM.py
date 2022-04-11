t = int(input())

for i in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    zipped = list(zip(a,b))
    zipped.sort(key = lambda x: x[0])

    for j in range(len(zipped)):
        if k >= zipped[j][0]:
            k += zipped[j][1]
        else:
            break
    print(k)