'''
384. Shuffle an Array
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

import collections
import random

def LeetCode384(ary):

    dict=collections.Counter(ary)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    fnl_lst=[]
    tmp=[]

    Combinations_recur(lst,cnt,fnl_lst,tmp,ary)

    return random.choice(fnl_lst)

def Combinations_recur(lst,cnt,fnl_lst,tmp,ary):

    if len(tmp)==len(ary):
        fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):

        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, fnl_lst, tmp,ary)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    ary=[1,2,3]
    print(LeetCode384(ary))

if __name__=='__main__':
    main()