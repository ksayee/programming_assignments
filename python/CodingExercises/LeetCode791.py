'''
791. Custom Sort String
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
'''

import collections

def Validate_String(tmp,S):

    lst=list(S)

    idx=tmp.index(S[0])
    j=1
    flg=False
    if idx<len(lst):
        idx=idx+1
        while idx<len(tmp):
            if tmp[idx]==lst[j]:
                if j==len(lst)-1:
                    flg=True
                    break
                idx=idx+1
                j=j+1
            else:
                idx=idx+1
    else:
        return False

    return flg

def LeetCode791(S,T):

    dict=collections.Counter(T)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,S,T)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp,S,T):

    if len(tmp)==len(T):
        flg=Validate_String(tmp,S)

        if flg==True:
            fnl_lst.append(''.join(tmp))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp, S,T)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    S='cba'
    T='abcd'
    print(LeetCode791(S,T))

if __name__=='__main__':
    main()