#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'minimumAverage' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY customers as parameter.
#

def minimumAverage(customers):
    customers.sort()
    
    total = 0
    curr_t = 0
    wait_t = 0
    min_heap = []
    i = 0
    while i < len(customers):
        if customers[i][0] <= curr_t:
            heapq.heappush(min_heap,(customers[i][1],customers[i][0]))
            i += 1
        elif min_heap:
            wait_t = curr_t - min_heap[0][1] + min_heap[0][0]
            total += wait_t
            curr_t += min_heap[0][0]
            heapq.heappop(min_heap)
        elif not min_heap: 
            heapq.heappush(min_heap,(customers[i][1],customers[i][0]))
            curr_t = customers[i][0]
            i += 1
        
    while min_heap:
        wait_t = curr_t - min_heap[0][1] + min_heap[0][0]
        total += wait_t
        curr_t += min_heap[0][0]
        heapq.heappop(min_heap) 
        
    return total // len(customers)
        
        
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers)

    fptr.write(str(result) + '\n')

    fptr.close()
