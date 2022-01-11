# -*- coding: utf-8 -*-
"""
Find majority element (Boyer–Moore Majority Vote Algorithm)
Given an integer array containing duplicates, return the majority element if present. A majority element appears more than n/2 times, where n is the array size.
For example, the majority element is 2 in array {2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2}.
"""

# Function to find the majority element present in a given list
def findMajorityElement(nums):
 
    # create an empty `HashMap`
    d = {}
 
    # store each element's frequency in a dictionary
    for i in nums:
        d[i] = d.get(i, 0) + 1
 
    # return the element if its count is more than `n/2`
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
 
    # no majority element is present
    return -1
 
 
if __name__ == '__main__':
 
    # assumption: valid input (majority element is present)
    nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
 
    result = findMajorityElement(nums)
    if result != -1:
        print('The majority element is', result)
    else:
        print('The majority element doesn\'t exist')



