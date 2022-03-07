#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(num):
    min_list = []
    max_list = []
    ans = []
    count = 0
    
    while count < len(num):
        
        count += 1
        
        if count %2 == 0:
            heapq.heappush(min_list, num[count -1])
        else:
            heapq.heappush(max_list, -num[count -1])
            
        if count > 1 and -1*max_list[0] > min_list[0]: 
            temp = max_list[0]
            heapq.heappushpop(max_list,-1 * min_list[0])
            heapq.heappushpop(min_list,-1 * temp)
        
        if count %2 == 0:
            ans.append(round((-1*max_list[0] + min_list[0])/ 2,1))
        else:
            ans.append(round(-1*max_list[0],1))
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
