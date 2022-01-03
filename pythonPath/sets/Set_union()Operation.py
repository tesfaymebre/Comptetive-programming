# Enter your code here. Read input from STDIN. Print output to STDOUT
n_Eng = input()
n_roll_num = set(input().split())
b_french = input()
b_roll_num = set(input().split())
print(len(n_roll_num.union(b_roll_num)))
