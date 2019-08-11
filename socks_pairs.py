#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count_socks = 0
    i = 0
    a = 0
    elemento = []
    for i in range(n):
        elemento = ar[i]
        if elemento != False:
            a=i+1
            while a < n:
                if elemento == ar[a]:
                    count_socks += 1
                    elemento = False
                    ar[a]= False
                    break
                a +=1
                    
        else:
            continue

    return count_socks

if __name__ == '__main__':
    ar= [2,7,5,4,3]
    n = len(ar)
    print(sockMerchant(n,ar))