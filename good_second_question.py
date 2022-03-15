import heapq

n, m = map(int,(input().split()))
heap = list(map(int,input().split()))
m = len(heap)

heapq.heapify(heap)
q = []
for i in range(n):
    q.append(int(input()))

di = dict()
count = 0
for val in sorted(q):
    if heap and val <= heap[0]:
        di[val] = count
    else: 
        while heap and val > heap[0]:
            heapq.heappop(heap)
            count += 1
        if not heap:
            di[val] = m
        else:
            di[val] = count

half = m // 2 
if m % 2 == 1:
    half = half + 1           
for x in q:
    if di[x] == 0 or di[x] >= half:
        print("NO")
    else:
        print("YES")