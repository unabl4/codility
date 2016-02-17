# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in range(1,n+1):
        P[k] = P[k-1] + A[k-1]
    return P[1:]


def solution(A):    
    ps = prefix_sums(A) # O(N)
    s  = ps[-1] # sum is the last prefix sum element
    min_diff = 2000 # largest possible diff: 1000 - -(1000)
    
    # O(N)
    for p in range(1,len(A)):
        left  = ps[p-1]
        right = s - left
        
        diff = abs(left-right)
        if diff < min_diff:
            min_diff = diff
    
    # 2 * O(N) => O(N)
    return min_diff