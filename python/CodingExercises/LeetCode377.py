'''
377. Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''

import collections

def LeetCode377(ary, tgt):

    fnl_lst=[]
    tmp=[]
    Combinations_recur(ary,fnl_lst,tmp,tgt)

    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,tgt):

    if tgt==0:
        if tmp not in fnl_lst:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(ary)):
        if ary[i]>tgt:
            break
        tmp.append(ary[i])
        Combinations_recur(ary, fnl_lst, tmp, tgt-ary[i])
        tmp.pop()

def main():

    ary=[1, 2, 3]
    tgt=4
    print(LeetCode377(ary,tgt))

if __name__=='__main__':
    main()