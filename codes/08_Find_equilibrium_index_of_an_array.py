# -*- coding: utf-8 -*-
"""
For an array A consisting n elements, index i is an equilibrium index if the sum of elements of subarray A[0…i-1] is equal to the sum of elements of subarray A[i+1…n-1]. i.e.

(A[0] + A[1] + … + A[i-1]) = (A[i+1] + A[i+2] + … + A[n-1]), where 0 < i < n-1

Similarly, 0 is an equilibrium index if A[1] + A[2] + … + A[n-1] sums to 0 and n-1 is an equilibrium index if A[0] + A[1] + … + A[n-2] sums to 0.

 
"""



# Function to find the equilibrium index of a list
def findEquilibriumIndex(A):
 
    # `left[i]` stores the sum of elements of sublist `A[0…i-1]`
    left = [0] * len(A)
 
    # traverse the list from left to right
    for i in range(1, len(A)):
        left[i] = left[i - 1] + A[i - 1]
 
    # `right` stores the sum of elements of sublist `A[i+1…n)`
    right = 0
 
    # maintain a list of indices
    indices = []
 
    # traverse the list from right to left
    for i in reversed(range(len(A))):
 
        ''' if the sum of elements of sublist `A[0…i-1]` is equal to
            the sum of elements of sublist `A[i+1…n)` i.e.
            `(A[0] + … + A[i-1]) = (A[i+1] + A[i+2] + … + A[n-1])` '''
 
        if left[i] == right:
            indices.append(i)
 
        # new right is `A[i] + (A[i+1] + A[i+2] + … + A[n-1])`
        right += A[i]
 
    print("Equilibrium Index found at", indices)
    
    
if __name__ == '__main__':
 
    A = [0, -3, 5, -4, -2, 3, 1, 0]
 
    findEquilibriumIndex(A)