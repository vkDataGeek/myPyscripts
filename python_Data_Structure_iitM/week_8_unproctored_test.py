def aboveaverage(l):
    (d,teamAvg,op)=({},0.0,[])
    sum_tot=0
    cnt_tot=0
    teamAvg=0.0
    for x,y in l:
        sum_tot += y
        cnt_tot += 1
        try:
            d[x].append(y)
        except:
            d[x]=[y]

    teamAvg=sum_tot/cnt_tot

    for x in d.keys():
        avg=sum(d[x])/len(d[x])
        if avg >= teamAvg:
            op.append(x)
    return op
