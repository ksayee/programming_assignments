'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

import collections

def LeetCode31(ary):

    sort_ary=sorted(ary)
    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key in sort_ary:
        if key not in lst:
            lst.append(key)
            cnt.append(dict[key])

    res_lst=[]
    tmp=[]
    Permutations_recur(ary,lst,cnt,res_lst,tmp)

    for i in range(0,len(res_lst)):
        if ary==res_lst[i]:
            if i==len(res_lst)-1:
                return res_lst[0]
            else:
                return res_lst[i+1]

def Permutations_recur(ary,lst,cnt,res_lst,tmp):

    if len(tmp)==len(ary):
        res_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Permutations_recur(ary,lst, cnt, res_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    ary=[1,2,3]
    print(LeetCode31(ary))

    ary = [3,2,1]
    print(LeetCode31(ary))

    ary = [1,1,5]
    print(LeetCode31(ary))

if __name__=='__main__':
    main()