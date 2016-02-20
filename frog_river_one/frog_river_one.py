# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    n = len(A)
    
    if n <= 0:
        return -1 # not reachable anyway
    
    s = X*(X+1)/2 # distance to travel
    
    left = {} # leaves left to visit
    
    # O(N)
    for i in range(1,(X+1)):
        left[i] = True
        
    # O(N)
    for index in range(n):
        pos = A[index] 
        if left[pos]: # not visited?
            left[pos] = False # mark as visited
            s -= pos
            
            if s <= 0: # exceeded the distance?
                return index # second
        
    return -1 # not found