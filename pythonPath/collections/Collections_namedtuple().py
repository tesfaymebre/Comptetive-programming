from collections import namedtuple
N,students = int(input()),namedtuple("students",input())
marks= [int((students._make(input().split())).MARKS) for i in range(N)]
print (round(sum(marks)/N,2))
