def reverse_loser(s):
    (op,i)=("",0)
    for sc in s.split(","):
        j=sc.split("-")
        (j[0],j[1])=(j[1],j[0])
        if i == 0:
            op=j[0]+"-"+j[1]
        else:
            op=op+","+j[0]+"-"+j[1]
        i+=1
    return(op)
    

def add_dict(d,k,v):
    try:
        d[k].append(v)
    except:
        d[k]=[v]
    

(match,players,results)=([],{},[])

while(True):
    in_data=input()
    if(in_data == ""):
        break
    match.append(in_data)

'''match=['Thiem:Medvedev:2-6,6-7,7-6,6-3,6-1', 'Barty:Osaka:6-4,6-4', 'Medvedev:Thiem:6-3,6-3', 'Osaka:Barty:1-6,7-5,6-2', 'Thiem:Medvedev:6-0,7-6,6-3', 'Osaka:Barty:2-6,6-2,6-0', 'Medvedev:Thiem:6-3,4-6,6-3,6-4', 'Barty:Osaka:6-1,3-6,7-5', 'Thiem:Medvedev:7-6,4-6,7-6,2-6,6-2', 'Osaka:Barty:6-4,1-6,6-3', 'Medvedev:Thiem:7-5,7-5', 'Osaka:Barty:3-6,6-3,6-3']
print(match)'''

for elm in match:
    data=elm.split(":")
    add_dict(players,data[0],data[2])
    add_dict(players,data[1],reverse_loser(data[2]))
    
'''print(players)'''


for player in players.keys():
    matches=players[player] 
    (won_5,won_3,won_sets,won_games,lost_sets,lost_games)=(0,0,0,0,0,0)
    for m in matches:
        sets=m.split(",")
        (won_s,lost_s)=(0,0)
        for s in sets:
            g=s.split("-")
            won_games+=int(g[0])
            lost_games+=int(g[1])
            if g[0]>g[1]:
                won_s+=1
            else:
                lost_s+=1

        won_sets+=won_s
        lost_sets+=lost_s
        
        if won_s == 3: 
            won_5+=1
        elif won_s == 2 and won_s + lost_s <= 3:
            won_3+=1

    '''print(player,won_5,won_3,won_sets,won_games,lost_sets,lost_games)'''
    results.append((player,won_5,won_3,won_sets,won_games,lost_sets,lost_games))
    
results.sort(key= lambda x: (x[5],x[6]))
results.sort(key= lambda x: (x[1],x[2],x[3],x[4]), reverse=True)
[ print(x[0],x[1],x[2],x[3],x[4],x[5],x[6]) for x in results ]









