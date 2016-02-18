# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A, K):
    # no rotation
    if K == 0:
        return A
        
    n = len(A)
    
    AP = [0] * n
    for i in range(n): # O(N)
        index = (i + K) % n
        AP[index] = A[i]
        
    return AP