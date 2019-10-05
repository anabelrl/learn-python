#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr2=[]
    while n > 0:
        num = arr[n-1]
        arr2.append(str(num))
        n -= 1
    print(" ".join(arr2))




