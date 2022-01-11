# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:17:36 2021

@author: hl3
"""


def findPair( array, target_sum ):
    array.sort()
    left = 0
    right = len( array ) - 1
    
    while left < right:
        current_sum =  array[right] - array[left]
        
        if current_sum == target_sum:
            return [ array[left], array[right] ]
        elif current_sum < target_sum:
            left = left + 1
        elif current_sum > target_sum:
            right = right - 1
            
    return None



A = [1, 5, 2, 2, 2, 5, 5, 4]
diff = 3

findPair(A, diff)