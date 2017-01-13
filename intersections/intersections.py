# solution
def solution(A):
    n = len(A) # number of 'discs'

    if n <= 1:
        return 0
        
    open_intervals = 1
    intersections  = 0
    
    enum   = list(enumerate(A)) # enumarate is exhaustive
    starts = map(lambda x: (x[0]-x[1], 1), enum) # O(n)
    ends   = map(lambda x: (x[0]+x[1], 2), enum) # O(n)

    discs = sorted(starts+ends, key=lambda x:x[0]) # n*log(n)
    end = discs[0][0]

    # 0..(n-1); O(n)
    for i in range(1, n*2):
        disc = discs[i]
        
        if disc[1] == 1: # start?
            open_intervals += 1
        else: # end?
            open_intervals -= 1
            if open_intervals > 0:
                intersections += (open_intervals)
            

    # special check
    if intersections > 1000000:
        return -1

    return intersections # n*log(n)

# print solution([1,5,2,1,4,0])
# print solution([1,0,1,2,1])
# print solution([1,2,3,4])
# print solution([1,0,1])