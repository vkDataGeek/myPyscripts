def remdup(l):
    ''' remdup: Remove duplicates, keeping last '''
    op=[]
    len_l=len(l)
    if len_l==0:
        return l
    else:
        for i in l:
            if i not in op:
                op.append(i)
            else:
                op.remove(i)
                op.append(i)
        return op


def splitsum(l):
    ''' returns list of Square of pos, cube of neg '''
    (pos,neg)=(0,0)
    for i in l:
        if i>=0:
            pos+= i**2
        else:
            neg+= i**3
    return [pos,neg]
         
    
def matrixflip(m,d):
    ''' returns horizontally/vertically flipped matrix '''
    op=m.copy()
    hv=[]
    if d == 'h':
        for x in op:
            row=x[:]
            row.reverse()
            hv.append(row)
        return(hv)
    elif d == 'v':
        op.reverse()
        return(op)            
    else:
        return(m)
