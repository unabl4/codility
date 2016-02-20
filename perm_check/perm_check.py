# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A) # N 
    
    elements = {} # dict
    
    # O(N)
    for e in A:
        elements[e] = elements.get(e,0) + 1
        
    # O(N)
    for i in range(1,(n+1)):
        occurrences = elements.get(i,0)
        if not occurrences == 1:
            return 0 # failure
        
    return 1 # success