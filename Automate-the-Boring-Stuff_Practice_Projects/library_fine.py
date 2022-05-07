# PROBLEM DESCRIPTION
# Your local library needs your help. Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). 
# The fee structure is as follows: 
# 1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)
# 2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date the fine is = (15 * number of days late) 
# 3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine is: fine = (500 * number of months late)
# 4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000.
# Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017 or December 31, 2017, if it is returned January 1, 2018, 
# that is a year late and the fine would be 10,000.
#
# Complete the libraryFine function in the editor below. 
# libraryFine has the following parameter(s): 
# d1, m1, y1: returned date day, month and year, each an integer 
# d2, m2, y2: due date day, month and year, each an integer 
#
#
# # The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2

import math
import os
import random
import re
import sys


def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if y1>y2:
        return 10000
    elif y1==y2 and m1 > m2:
        return 500*(m1-m2)
    elif y1==y2 and m1 == m2 and d1>d2:
        return 15*(d1-d2)
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
