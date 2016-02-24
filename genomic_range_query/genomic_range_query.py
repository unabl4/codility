# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S, P, Q):
    n = len(S) # length of genome
    m = len(P) # number of queries

    nuc = {"A": 0, "C": 1, "G": 2, "T": 3} # nucleotide impact factor index
    arr = [[0] * 4 for r in range(n)] # n*4 matrix
    
    # O(N)
    for i in range(n):
        c  = S[i]   # nucleotide char
        ni = nuc[c] # nucleotide index
        arr[i][ni] = 1
        
    # prefix sums (O(N)):
    for i in range(1,n):
        for j in range(4):
            arr[i][j] += arr[i-1][j]
            
    # queries O(M):
    results = [0]*m
    
    for i in range(m):
        x = P[i]
        y = Q[i]
        
        # 0..3
        for a in range(4):
            top = 0
            if x-1 >= 0:
                top = arr[x-1][a] 
                
            if arr[y][a]-top > 0:
                results[i] = a+1
                break # found
            
    # 2 * O(N) + O(M) => O(N+M)
    return results