'''
Form minimum number from given sequence
Given a pattern containing only I’s and D’s. I for increasing and D for decreasing.
Devise an algorithm to print the minimum number following that pattern. Digits from 1-9 and digits can’t repeat.
Examples:
   Input: D        Output: 21
   Input: I        Output: 12
   Input: DD       Output: 321
   Input: II       Output: 123
   Input: DIDI     Output: 21435
   Input: IIDDD    Output: 126543
   Input: DDIDDIID Output: 321654798
'''

def Validate(tmp,seq):

    k=0
    for i in range(1,len(tmp)):
        if seq[k]=='D':
            if tmp[i]<tmp[i-1]:
                pass
            else:
                return False
        elif seq[k]=='I':
            if tmp[i]>tmp[i-1]:
                pass
            else:
                return False
        if k==len(seq)-1:
            pass
        else:
            k=k+1
    return True

def Combinations_recur(lst,cnt,tmp,final_lst,seq):

    if len(tmp)==len(lst):
        flg=Validate(tmp,seq)
        if flg==True:
            final_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, final_lst, seq)
        cnt[i]=cnt[i]+1
        tmp.pop()

def FormMinimumNumberGivenSequence(seq):

    lst=[]
    cnt=[]
    k=0
    while k<=len(seq):
        k=k+1
        lst.append(str(k))
        cnt.append(1)

    tmp=[]
    final_lst=[]

    Combinations_recur(lst,cnt,tmp,final_lst,seq)
    if len(final_lst)>0:
        return ''.join(final_lst[0])
    else:
        return -1

def main():
    
    seq='D'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'I'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'DD'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'II'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'DIDI'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'IIDDD'
    print(FormMinimumNumberGivenSequence(seq))

    seq = 'DDIDDIID'
    print(FormMinimumNumberGivenSequence(seq))

if __name__=='__main__':
    main()