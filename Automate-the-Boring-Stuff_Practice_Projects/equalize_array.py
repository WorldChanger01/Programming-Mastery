# HACKER RANK PROBLEM DESCRIPTION
#
# Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.
#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import math
import os
import random
import re
import sys


def equalizeArray(arr):
    arr_dict ={}
    for elem in arr:
        if elem not in arr_dict:
            arr_dict[elem] = 1
        else:
            arr_dict[elem] += 1
            
    # The variable len_num_equal_val is the length of the number with equal values    
    len_num_equal_val = max(arr_dict.values())
    
    return len(arr) - len_num_equal_val
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
