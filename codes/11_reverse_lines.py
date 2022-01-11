# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 08:10:08 2021

@author: hl3
"""

def reverseList( array ):
    start, end = 0, len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start = start + 1
        end = end - 1
        
        
def reverseWordsInString( string ):
    words = []
    startOfWord = 0
    for idx in range( len(string)):
        character = string[idx]
        
        if character == " ":
            words.append( string[startOfWord: idx ] )
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
            
    words.append( string[startOfWord: ] )
    
    reverseList(words)
    
    return "".join(words)



reverseWordsInString("hi harsha")