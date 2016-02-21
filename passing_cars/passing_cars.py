# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    ones = 0
    s = 0
    
    # O(N)
    for i in A:
        if i == 1:
            ones += 1
          
    # O(N)  
    for i in A:
        if i == 0:
            s += ones
        else:
            ones -= 1
            
    if s > 1000000000:
        return -1
            
    return s