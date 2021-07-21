# -*- coding: utf-8 -*-
"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should nd all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the target sum, the function should return an empty array.

Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0

Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""

def threeNumberSum( array, target_sum ):
    array.sort()
    triplets = []
    
    for i in range( len(array) - 2 ):
        left =i + 1
        right = len( array ) - 1
        
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target_sum:
                triplets.append([ array[i], array[left], array[right] ])
                left = left + 1
                right = right - 1
                
            elif current_sum < target_sum:
                left = left + 1
            elif current_sum > target_sum:
                right = right - 1
                
    return triplets

print( threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0 ) )

