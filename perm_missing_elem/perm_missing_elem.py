# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    n = len(A)
    
    if n <= 0:
        return 1
    
    exist = [False] * (n+2) # O(N)
    
    # O(N)
    for element in A:
        exist[element] = True
      
    # O(N)
    for index in range(1,n+2):
        if not exist[index]:
            return index # 3 * O(N) => O(N)