'''
254. Factor Combinations
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''

import collections

def Get_Factors(num):

    lst=[]
    for i in range(2,num):
        if num%i==0:
            lst.append(i)
    return lst

def LeetCode254(num):

    lst=Get_Factors(num)
    fnl_lst=[]
    tmp=[]
    rem=0
    Combinations_recur(lst,fnl_lst,tmp,num,rem)

    return fnl_lst

def Combinations_recur(lst,fnl_lst,tmp,num,rem):

    if num==1 and rem==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(lst)):
        if lst[i]>num:
            break
        tmp.append(lst[i])
        Combinations_recur(lst, fnl_lst, tmp, int(num/lst[i]),num%lst[i])
        tmp.pop()

def main():

    num=1
    print(LeetCode254(num))

    num = 8
    print(LeetCode254(num))

    num= 12
    print(LeetCode254(num))

    num = 37
    print(LeetCode254(num))

    num = 32
    print(LeetCode254(num))

if __name__=='__main__':
    main()