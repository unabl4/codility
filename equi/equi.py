# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # null input fix
    if len(A) == 0:
        return -1
    elif len(A) == 1:
        return 0
    
    s = sum(A) # total sum; O(n)
    left,right = 0,s
    
    # O(n)
    for index in range(0,len(A)):
        right -= A[index]
        
        if left == right:
            return index    # stop here
        else:
            left += A[index]
            
    return -1
    # 2 * O(n) => O(n)
