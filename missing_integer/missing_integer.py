# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import sys
MAX_INT = sys.maxint

# ignore negative and zero numbers
def correct(n):
    if n <= 0:
        return MAX_INT
    return n

def solution(A):
    dict = {}
    min_a = MAX_INT # min existing element
    
    # O(N)
    for element in A:
        # skip negative elements
        if element <= 0:
            continue # skip
        
        if element < min_a:
            min_a = element
            
        dict[element] = True # exists
        
    min_na = MAX_INT
    
    # O(N)
    for existing in dict.keys():
        left  = existing - 1 # previous
        right = existing + 1 # next
        
        left_exist  = dict.get(left, False)
        right_exist = dict.get(right, False)
        
        if not left_exist and not right_exist:            
            m_na = min(correct(left), correct(right))
        elif not left_exist:
            m_na = correct(left)
        elif not right_exist:
            m_na = correct(right)
                
        # update min
        if m_na < min_na:
            min_na = m_na
        
    if min_a > 1 or min_a <= 0:
        return 1
    else:
        return min_na