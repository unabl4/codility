# solution
def solution(S):
    n = len(S)
    s = [] # stack
    m = { "(": ")", "{": "}", "[": "]" } # mapping
    for i in range(n):
        if S[i] == "(" or S[i] == "{" or S[i] == "[": # beginning?
            s.append(S[i]) # add to stack
        else:
            if(not s): # check if stack is empty
                return 0 # must not be empty
            t = s.pop() # retrieve from stack
            if(S[i] != m.get(t)):
                return 0 # does not match

    return (not s) & 1 # !s; must be empty

# print solution("") # empty string, 1
# print solution("{[()()]}") # 1
# print solution("([)()]") # 0