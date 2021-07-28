# -*- coding: utf-8 -*-
"""
validate sub sequence

"""




nums = [ 5,1,22,25,6,-1,8,10 ]
sequence = [ 1,6,-1, 10 ]


# not able to use set. This is due cannot handle duplicate elements;



def is_validsubsequence( array, sequence ):
    seq_idx = 0
    for value in array:
        if seq_idx == len(array):
            break
        
        if sequence[ seq_idx ] == value:
            seq_idx = seq_idx + 1
            
    return seq_idx == len(sequence)

def isValidSubsequence(array, sequence):
    arrIdx = 0 
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)



print( is_validsubsequence( nums, sequence))
