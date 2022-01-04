T = int(input())
for i in range(T):
    a_b = input().split()
    try:
        print(int(a_b[0])//int(a_b[1]))
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print ("Error Code:",e)
