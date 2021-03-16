
### Longest Common Sequence ###
def LCS(u,v):     # u[0..m-1], v[0..n-1]
    for r in range(len(u)+1):
        LCS[r][len(v)+1] = 0    # r for row

    for c in range(len(v)+1):
        LCS[len(u)+1][c] = 0    # c for col

    for c in range(len(v), -1, -1):
        for r in range(len(u), -1, -1):
            if (u[r] == v[c]):
                LCS[r][c] = 1 + LCS[r+1][c+1]
            else:
                LCS[r][c] = max(LCS[r+1][c], LCS[r][c+1])
    return(LSC[0][0])

### Longest Common Word ###
def LCW(u,v):     # u[0..m-1], v[0..n-1]
    for r in range(len(u)+1):
        LCW[r][len(v)+1] = 0    # r for row

    for c in range(len(v)+1):
        LCW[len(u)+1][c] = 0    # c for col

    maxLCW = 0
    for c in range(len(v)+1, -1, -1):
        for r in range(len(u)+1, -1, -1):
            if (u[r] == v[c]):
                LCW[r][c] = 1 + LCW[r+1][c+1]
            else:
                LCW[r][c] = 0
            if LCW[r][c] > maxLCW:
                maxLCW = LCW[r][c]
    return(maxLCW)
            
        

