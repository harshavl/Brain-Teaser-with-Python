

# O(n) and O(1)
# first solution using Bucket sorting;


def threeNumberSort( array, order ):
    firstValue = order[0]
    secondValue = order[1]
    
    #keep track of the indicies where the values are stored
    firstIdx, secondIdx, thirdIdx = 0, 0, len(array) - 1
    
    while secondIdx <= thirdIdx:
        value = array[secondIdx]
        
        if value == firstValue:
            array[secondIdx], array[firstIdx] = array[firstIdx],array[secondIdx]
            firstIdx = firstIdx + 1
            secondIdx = secondIdx + 1
            
        elif value == secondValue:
            secondIdx = secondIdx + 1
            
        else:
            # value == thirdIdx
            print(value)
            array[secondIdx], array[thirdIdx] = array[thirdIdx], array[secondIdx]
            thirdIdx = thirdIdx - 1
            
    return array


A = [ 1,0,0,-1,-1,0,1,1]
order = [ 0,1,-1 ]
print( threeNumberSort( A, order))
    