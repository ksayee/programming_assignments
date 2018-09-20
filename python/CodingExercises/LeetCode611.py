'''
611. Valid Triangle Number
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
'''

import collections
def LeetCode611(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp)

    return fnl_lst

def Combinations_recur(lst,cnt,fnl_lst,tmp):

    if len(tmp)==3:

        a=tmp[0]
        b=tmp[1]
        c=tmp[2]
        if a+b>c and a+c>b and b+c>a:
            if sorted(tmp) not in fnl_lst:
                fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst,cnt, fnl_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=[2,2,3,4]
    print(LeetCode611(ary))


if __name__=='__main__':
    main()