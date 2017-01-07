# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A) # [A] - list
    
    if(n < 3):
        return 0
        
    A.sort() # ascending (N * log(N))
    a1 = A[0] * A[1] * A[2]
    a2 = A[0] * A[1] * A[n-1]
    a3 = A[0] * A[n-2] * A[n-1]
    a4 = A[n-3] * A[n-2] * A[n-1]
    return max(a1,a2,a3,a4)
