# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

import math

def solution(A, B, K):
    left = int(math.ceil(A / float(K))) * K
    return int(math.floor((B-left)/float(K))) + 1