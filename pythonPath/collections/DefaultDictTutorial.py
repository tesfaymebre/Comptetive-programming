from collections import defaultdict
sizes = list(map(int,input().split()))
groupA = defaultdict(list)
for i in range(1,sizes[0]+1):
    A = input()
    groupA[A].append(str(i))
for j in range(sizes[1]):
    groupB = input()
    if groupB in groupA:
        for x in groupA[groupB]:
            print(x,end=" ")
    else:
        print(-1,end=" ")
    print()
