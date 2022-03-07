#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while len(A) > 1 and A[0] < k:
        temp = heapq.heappop(A)
        re = min(temp,A[0]) + 2*max(temp,A[0])
        heapq.heappushpop(A,re)
        
        count += 1
        
    if A[0] < k:
        return -1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
