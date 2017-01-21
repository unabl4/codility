# solution
def solution(S):
    n = len(S)
    s = [] # stack
    for i in range(n):
        if S[i] == "(": # beginning?
            s.append(S[i]) # add to stack
        else:
            if(not s): # check if stack is empty
                return 0 # must not be empty
            t = s.pop() # retrieve from stack
            if(S[i] != ")"):
                return 0 # does not match

    return (not s) & 1 # !s; must be empty