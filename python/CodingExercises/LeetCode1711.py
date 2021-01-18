'''
1711. Count Good Meals
A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
You can pick any two different foods to make a good meal.
Given an array of integers deliciousness where deliciousness[i] is the
deliciousness of the i​​​​​​th​​​​​​​​ item of food, return the number of different good meals you can make from this list modulo 109 + 7.
Note that items with different indices are considered different even if they have the same deliciousness value.
Example 1:
Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:
Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
'''

import collections
import math

def Validate(tmp):

    return math.log2(sum(tmp)).is_integer()

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==2:
        flg = Validate(tmp)
        if flg is True:
            if sorted(tmp) not in fnl_lst:
                fnl_lst.append(sorted(tmp.copy()))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def LeetCode1711(deliciousness):

    dict =collections.Counter(deliciousness)

    lst =[]
    cnt = []

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp = []
    fnl_lst = []
    Combinations_recur(lst,cnt,tmp,fnl_lst)

    return fnl_lst

def main():

    deliciousness = [1, 3, 5, 7, 9]
    print(LeetCode1711(deliciousness))

    deliciousness = [1,1,1,3,3,3,7]
    print(LeetCode1711(deliciousness))

if __name__=='__main__':
    main()