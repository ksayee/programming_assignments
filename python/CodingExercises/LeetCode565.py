'''
565. Array Nesting
Medium
A zero-indexed array A of length N contains all integers from 0 to N-1.
Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]…
By that analogy, we stop adding right before a duplicate element occurs in S.
Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
'''

import collections

def Validate(tmp,ary):

    k=0
    flg=True
    while k<len(tmp):
        val=tmp[k]
        k=k+1
        try:
            if tmp.index(ary[val])==k:
                if k==len(tmp)-1:
                    break
                else:
                    pass
            else:
                flg=False
                break
        except:
            flg=False
            break
    return flg

def Combinations_recur(lst,cnt,tmp,fnl_lst,ary):

    if len(tmp)>0:
        flg=Validate(tmp,ary)
        if flg==True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,ary)
        tmp.pop()
        cnt[i]=cnt[i]+1

def LeetCode565(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,ary)
    return sorted(fnl_lst,key=lambda x:len(x),reverse=True)[0]

def main():

    ary=[5,4,0,3,1,6,2]
    print(LeetCode565(ary))

if __name__=='__main__':
    main()