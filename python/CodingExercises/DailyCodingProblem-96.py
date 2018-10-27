'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Given a number in the form of a list of digits, return all possible permutations.
For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],
[3,1,2],[3,2,1]].
'''

import collections
def DailyCodingProblem96(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]

    Combinations_recur(ary,lst,cnt,tmp,fnl_lst)

    return fnl_lst

def Combinations_recur(ary,lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(ary):
        fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):

        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(ary, lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def main():

    ary=[1,2,3]
    print(DailyCodingProblem96(ary))

if __name__=='__main__':
    main()