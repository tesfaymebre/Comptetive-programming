if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    A = [x for x in arr]
    for i in range(n-1):
        for j in range(i+1,n):
            if A[j] < A[i]:
                curr = A[i]
                A[i] = A[j]
                A[j] = curr
    for j in range(len(A)-1,-1,-1):
        if A[j] != A[j-1]:
            print(A[j-1])
            break
