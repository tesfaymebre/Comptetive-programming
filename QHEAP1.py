import math
import os
import random
import re
import sys
import heapq

nums = []
deleted = set()

def query(q_val):
    
    if q_val[0] == 1:
        if q_val[0] in deleted:
            deleted.remove(q_val[0])
            
        heapq.heappush(nums, q_val[1])
            
    elif q_val[0] == 2:
        deleted.add(q_val[1])

    else:
        while nums[0] in deleted:
            deleted.remove(nums[0])
            heapq.heappop(nums)
            
        print(nums[0])

    return
            
def main():    
    n = int(input())
    
    for i in range(n):
        query(list(map(int,input().rstrip().split())))
        
main()    

