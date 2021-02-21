def rainaverage(l):
    ''' get average per key '''
    (d,op)=({},[])
    
    for (x,y) in l:
        if x in d.keys():
            val=d[x]
            val=val.append(y)
        else:
            d[x]=[y]

    for k in d.keys():
        op.append((k,sum(d[k])/len(d[k])))

    return op   



def listtype(l):
  return(type(l) == type([]))

def flatten(l):
    if l == []:
        return l

    if listtype(l[0]):
        return flatten(l[0]) + flatten(l[1:])
    return l[:1] + flatten(l[1:])

