(ip_seq,StoredBest)=([],[])
N=int(input())
if N > 2500:
    N=2500

for i in range(N):
    ip_seq.append(int(input()))

print("input Seq: ", ip_seq)

        
#StoredBest= [0] * N    ## whenever Best(j) is computed, store the value StoredBest[j].
for k in range(N):
  StoredBest.append(0)


## Using Memoization
def Best_memo(i):
    if StoredBest[i] != 0:      #Not 0, so Best(i) has already been computed.
        return StoredBest[i]    #so just lookup the array and return value.

    if i== 0:
        StoredBest[i]=1
        return 1
    else:
        max_s=1
        for j in range(i):
            if ip_seq[i] % ip_seq[j] == 0:
                if StoredBest[j] != 0:  #Best(j) already computed
                    temp=StoredBest[j]
                else:
                    temp=Best(j)        #Best(j) has to be computed
                    max_s=max(max_s, temp+1)
        
        StoredBest[i]=max_s     #Now that we have computed the value store it so that it can be reused.
        return max_s



###Using DP
def Best_dp():
    StoredBest[0]=1
    for i in range(N):
        max_d=1
        for j in range(i):
            if ip_seq[i] % ip_seq[j] == 0:
                max_d=max(max_d, StoredBest[j]+1)
        StoredBest[i]=max_d
        

Best_dp()
print("Max_val: ", max(StoredBest))


### This Best(i) calculation has lot of irrelevant recursion ####
def Best_recur(i):
    if i == 0:
        return 1
    else:
        max_c=1
        for j in range(i):
            if ip_seq[i] % ip_seq[j] == 0:
                max_c=max(max_c, Best_recur(j)+1)
        return max_c

