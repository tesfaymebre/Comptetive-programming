# Enter your code here. Read input from STDIN. Print output to STDOUT
n_m = input().split()
n = int(n_m[0])
m = int(n_m[1])

nArr = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for i in range(n):
    if nArr[i] in A:
        happiness+=1
    if nArr[i] in B:
        happiness-=1

print(happiness)
