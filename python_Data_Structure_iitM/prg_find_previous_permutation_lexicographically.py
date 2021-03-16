from itertools import permutations 
  
def lexicographical_permutation(str): 
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    for x in perm: 
        print(x) 

def lexicographical_permutation_l(str): 
    perm = sorted(''.join(chars) for chars in permutations(str)) 
    return perm
        
def lexicographical_prev_permutation(str): 
    ''' get all permutations & find previous in Dict'''
    print("Given String: ", str)
    perm = sorted(''.join(chars) for chars in permutations(str))
    str_pos=perm.index(str)
    if str_pos == 0:
        op_str=str   ##No previous permutation"
    else:
        op_str=perm[str_pos-1]
    print("Previous lexicographic String: ", op_str)

str ='ghadbicefj'
#print(lexicographical_permutation_l(str))
lexicographical_prev_permutation(str)
