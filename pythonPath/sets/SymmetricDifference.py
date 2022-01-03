# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
M_vals = set(map(int,input().split()))
N = input()
N_vals = set(map(int,input().split()))
sym_diff = (M_vals.difference(N_vals)).union(N_vals.difference(M_vals))
sym_diff_sorted = list(sym_diff)
sym_diff_sorted.sort()

for i in range(len(sym_diff)):
    print(sym_diff_sorted[i])
