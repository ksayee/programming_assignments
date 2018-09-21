'''
870. Advantage Shuffle
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.



Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
'''

import collections

def GetMax_Count(lst1,lst2):

    cnt=0
    for i in range(0,len(lst1)):

        if lst1[i]>lst2[i]:
            cnt=cnt+1

    return cnt

def LeetCode870(a,b):

    dict=collections.Counter(a)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst={}
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,a,b)

    return sorted(fnl_lst.items(),key=lambda x:x[0],reverse=True)[0]

def Combinations_recur(lst,cnt,fnl_lst,tmp,a,b):

    if len(tmp)==len(a):

        count=GetMax_Count(tmp,b)
        if count in fnl_lst.keys():
            fnl_lst[count].append(tmp.copy())
        else:
            res=[]
            res.append(tmp.copy())
            fnl_lst[count]=res

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp, a, b)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    a=[2,7,11,15]
    b=[1,10,4,11]
    print(LeetCode870(a,b))

    a = [12,24,8,32]
    b = [13,25,32,11]
    print(LeetCode870(a, b))

if __name__=='__main__':
    main()