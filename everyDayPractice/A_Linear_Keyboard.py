t = int(input())
min_time = []
for i in range(t):
    keyboard = input()
    s = input()
    time = 0
    for j in range(len(s)-1):
        time += abs((keyboard.find(s[j+1])+1)-(keyboard.find(s[j])+1))
    min_time.append(time)
print(*min_time,sep = "\n")
