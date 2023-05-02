#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    r = n-2
    temp = arr[n-1]
    
    for n in range(n-1, 0 , -1):
        if arr[r] > temp:
            arr[r+1] = arr[r]
        else:
            arr[r+1] = temp
        print(*arr)
        r = r-1
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
