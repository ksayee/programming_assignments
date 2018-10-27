'''
This problem was asked by Facebook.
Given a list of integers, return the largest product that can be made by multiplying any three
integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 *
-10 * 5.
'''

import collections
def DailyCodingProblem69(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]

    Combinations_recur(lst,cnt,tmp,fnl_lst)

    out_dict={}
    for lst in fnl_lst:
        prd=1
        for l in lst:
            prd=prd*l
        if prd in out_dict.keys():
            out_dict[prd].append(lst)
        else:
            tmp=[]
            tmp.append(lst)
            out_dict[prd]=tmp
    return sorted(out_dict.items(),key=lambda x:x[0],reverse=True)[0]


def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==3:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp).copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=[-10, -10, 5, 2]
    print(DailyCodingProblem69(ary))

if __name__=='__main__':
    main()