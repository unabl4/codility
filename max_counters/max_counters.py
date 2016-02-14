# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    n = len(A) # number of operations; M

    # declare counters
    counters = {}

    # set initial state; O(N)
    counters = {} # create counters` row
    for i in range(0,N):
        counters[i] = 0

    # counters' max value
    max_value = set_max_value = 0

    # go through operations; O(M)
    for op_index in range(0,n):
        ctr = A[op_index] # counter number

        if 1 <= ctr and ctr <= N: # increase(x)
            old_value = counters[ctr-1]

            if old_value < set_max_value:
                counters[ctr-1] = set_max_value + 1
            else:
                counters[ctr-1] += 1

            # max value update
            value = counters[ctr-1]
            if value > max_value:
                max_value = value

        elif ctr == N+1: # max counter operation
            set_max_value = max_value # O(1)


    # correct max values; O(N)
    for i in range(0,N):
        value = counters[i]
        if value < set_max_value:
            counters[i] = set_max_value

    return counters.values()
