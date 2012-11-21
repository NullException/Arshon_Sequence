# -*- coding: utf-8 -*-'
from random import Random
# проверка на корректность последовательности
def Good_Arshon_Sequence(arshon_sequence,k):
    is_good=True
    exit=False
    half=(k+1)/2
    t=1
    while is_good and not exit:
        is_good=False
        j=0
        i=k-t
        while j<t and not is_good:
            is_good= arshon_sequence[k-j] != arshon_sequence[i-j]
            j+=1
        t+=1
        exit= t>half
    return is_good
#составление последовательности
def Make_Arshon_Sequence(n):
    arshon_sequence=[0]*n
    arshon_sequence[0]=1
    s=0
    k=1
    while (k>=1 and k<=n-1):
        arshon_sequence[k]+=1
        if arshon_sequence[k]==4:
            arshon_sequence[k]=0
            k-=1
        else:
            if Good_Arshon_Sequence(arshon_sequence,k):
                k+=1
                if k==n:
                    s+=1
                    print arshon_sequence
                    k=n-1
    return s
            


if __name__ == '__main__':
    r=Random()
    n=r.randint(1,10)
    print n
    s=Make_Arshon_Sequence(n)
    print s
