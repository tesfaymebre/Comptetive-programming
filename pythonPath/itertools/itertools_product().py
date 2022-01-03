from itertools import product
A = map(int,input().split())
B = map(int,input().split())
cartesian_pro = tuple(product(A,B))
for i in range(len(cartesian_pro)):
    print(cartesian_pro[i],end = " ")
