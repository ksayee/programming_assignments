'''
719. Find K-th Smallest Pair Distance
Hard
Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.
Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
'''

import collections

def GetDiff(tmp):
    return abs(tmp[0]-tmp[1])

def Combinations_recur(lst,cnt,tmp,output_dict):

    if len(tmp)==2:
        diff=GetDiff(tmp)
        if diff in output_dict.keys():
            output_dict[diff].append(tmp.copy())
        else:
            output_dict[diff]=[]
            output_dict[diff].append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, output_dict)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode719(ary):

    dict=collections.Counter(ary)
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    output_dict={}
    Combinations_recur(lst,cnt,tmp,output_dict)
    return sorted(output_dict.items(),key=lambda x:x[0])[0]

def main():

    ary=[1,3,1]
    print(LeetCode719(ary))

if __name__=='__main__':
    main()