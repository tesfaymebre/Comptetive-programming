n, m = map(int,input().split())

show_up = []
for i in range(m):
    show_up.append(tuple(map(int,input().split())))

show_up.sort()
p1 = show_up[0][0]
p2 = show_up[0][1]

for i in range(1,len(show_up)):
    if (abs(p2 - show_up[i][0]) <= 1 or p2 >= show_up[i][0]) and p2 <= show_up[i][1]:
         p2 = show_up[i][1]

print("NO" if p1 == 0 and p2 == n - 1 else "YES")

