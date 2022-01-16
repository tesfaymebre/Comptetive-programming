#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    occurance_a = 0
    for x in s:
        if x == 'a':
            occurance_a+=1

    occurance_a = occurance_a * (n //len(s))
    remainder = n % len(s)
    for j in range(remainder):
        if s[j] == 'a':
            occurance_a += 1
    return occurance_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
