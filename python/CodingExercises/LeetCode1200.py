'''
1200. Minimum Absolute Difference
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==2:
        diff=abs(tmp[0]-tmp[1])
        if diff in fnl_lst.keys():
            if sorted(tmp) not in fnl_lst[diff]:
                fnl_lst[diff].append(sorted(tmp))
        else:
            fnl_lst[diff]=[]
            fnl_lst[diff].append(sorted(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1200(lst):

    dict=collections.Counter(lst)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst={}
    Combinations_recur(lst,cnt,tmp,fnl_lst)
    return sorted(fnl_lst.items(),key=lambda x:x[0])[0][1]

def main():

    lst=[4,2,1,3]
    print(LeetCode1200(lst))

    lst = [1,3,6,10,15]
    print(LeetCode1200(lst))

    lst = [3,8,-10,23,19,-4,-14,27]
    print(LeetCode1200(lst))

if __name__=='__main__':
    main()