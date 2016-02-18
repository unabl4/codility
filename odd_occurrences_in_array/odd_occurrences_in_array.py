# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A)
    
    O = {} # occurences table
    for element in range(n): # O(N)
        x = A[element]
        O[x] = O.get(x,0) + 1
        
    # O(N)
    for (a,b) in O.items():
        if b % 2 == 1: # odd
            return a