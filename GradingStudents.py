#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    finalGrade = []
    for grade in grades:
        if grade < 38:
            finalGrade.append(grade)
            # 63 % 5 // 12 r = 3  if remainder 4,5  it will round to the next level 
        elif (5 - grade % 5) <= 2:
            add = 5- grade  % 5
            print(add)
            finalGrade.append(grade+add)
        else:
            finalGrade.append(grade)    
                
    return finalGrade        
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
