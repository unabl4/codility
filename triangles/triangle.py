# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    n = len(A)
    if(n < 3):
        return 0; # no triangles
        
    A.sort() # N*log(N)
    for i in range(n-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
                        
    return 0