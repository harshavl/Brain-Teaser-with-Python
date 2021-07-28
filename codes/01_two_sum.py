'''
Problem Statement
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10 Sample output: [-1, 11]
'''



def twoNumberSum( array, target_sum ):
    hash_nums = {}
    for num in array:
        potentialmatch = target_sum - num
        if potentialmatch in hash_nums:
            return [ potentialmatch, num ]
        else:
            hash_nums[num] = True
            
    return []


def twoNumberSum2( array, target_sum ):
    array.sort()
    left = 0
    right = len( array ) - 1
    
    while left < right:
        current_sum = array[left] + array[right]
        
        if current_sum == target_sum:
            return [ array[left], array[right] ]
        elif current_sum < target_sum:
            left = left + 1
        elif current_sum > target_sum:
            right = right - 1
            
    return None




print( twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10 ))

print( twoNumberSum2( [3, 5, -4, 8, 11, 1, -1, 6], 10 ))