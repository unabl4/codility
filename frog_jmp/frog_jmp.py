# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(X, Y, D):
    return int(math.ceil((Y-X)/float(D)))