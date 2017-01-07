# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    elements = {}
    
    # O(n)
    for i in range(len(A)):
        elements[A[i]] = True
        
    return len(elements) # number of keys
