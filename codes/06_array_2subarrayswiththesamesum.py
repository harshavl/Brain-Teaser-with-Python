# -*- coding: utf-8 -*-
"""


Partition an array into two subarrays with the same sum
Input:  {6, -4, -3, 2, 3}
 
Output: The two subarrays are {6, -4} and {-3, 2, 3} having equal sum of 2
 
 
Input:  {6, -5, 2, -4, 1}
 
Output: The two subarrays are {} and {6, -5, 2, -4, 1} having equal sum of 0


Logic:
sum of right subarray = total sum – sum of elements so far

A = [ 6, -4, -3, 2, 3 ]
[6, -4]
[-3, 2, 3]
    
"""




# Partition the list into two sublists with the same sum
def partition(A):
 
    # do for each element in the list
    for i in range(len(A)):
        left_sum = 0
        for j in range(i):
            left_sum += A[j]
 
        right_sum = 0
        for j in range(i, len(A)):
            right_sum += A[j]
 
        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if left_sum == right_sum:
            return i
 
    # invalid input
    return -1


    

A = [ 6, -4, -3, 2, 3 ]
i = partition(A)

if i != -1:
    print( A[:i] )
    print( A[i:] )
else:
    print("The list can't be partitioned")
    



