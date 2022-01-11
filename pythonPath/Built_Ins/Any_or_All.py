N = int(input())
integers = list(map(int,input().split()))
print (all([x > 0 for x in integers]) and
    any([y==int(str(y)[::-1]) for y in integers]))

    
