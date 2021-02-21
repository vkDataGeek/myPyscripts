
def is_prime(n):
    '''is_prime : check if num is prime '''
    if(n==1):
        return False
    elif(n <= 0):
        return False
    i=2
    while(i <= n//2):
        if(n%i ==0):
            return False
        i+=1
    return True


def primepartition(m):
    ''' primepartition: check for partitioned prime exist '''
    if(m <= 1):
        return False
    p=1
    while (p <= m//2 +1):
        q=m-p
        p_prime=is_prime(p)
        q_prime=is_prime(q)
        if(p_prime and q_prime):
            return True
        p+=1
    return False


def matched(s):
    ''' matched: check for ( ) are matched '''
    open_br_cnt=s.count('(')
    close_br_cnt=s.count(')')
    
    if(open_br_cnt != close_br_cnt):
        return False
    else:
        temp=[]
        match=True
        index=0
        while index < len(s) and match:
            char=s[index]
            if char == '(':
                temp.append(char)
            elif char == ')':
                if len(temp) == 0:
                    match=False
                else:
                    temp.pop()
            index+=1

        return match and len(temp) == 0

        

def rotatelist(l,k):
    ''' rotatelist : rotate elements by k char '''
    new_list=l[:]
    len_l=len(l)
    if(k <= 0):
        return new_list
    elif(len_l < 2):
        return new_list
    else:
        for i in range(0,k):
            temp=new_list[:]
            for j in range(0,len_l):
                new_list[j-1]=temp[j]
        return new_list

def rotatelist_1(l,k):
    ''' rotatelist : rotate elements by k char '''
    new_list=l[:]
    len_l=len(l)
    if(k <= 0):
        return print(new_list)
    elif(len_l < 2):
        return print(new_list)
    else:
        for i in range(0,k):
            temp=new_list[:]
            for j in range(0,len_l):
                new_list[j-1]=temp[j]
        return print(new_list)

    




        















            
        














    

