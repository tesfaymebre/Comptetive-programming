# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
distinct_country = set()
for i in range(N):
    distinct_country.add(input())
print(len(distinct_country))
