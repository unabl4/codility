# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # negative number protection
    if N < 0:
        return 0

    n = bin(N)[2:] # binary representation

    # indicators
    left_index  = -1
    longest_gap = 0 # max gap

    for i in range(0,len(n)):
        if n[i] == '1':
            if left_index == -1: # not started
                left_index = 0
            else: # already started
                gap = i - left_index - 1 # correct index bounds
                if gap > longest_gap:
                    longest_gap = gap # update longest gap

                # update indexes
                left_index = right_index = i


    return longest_gap