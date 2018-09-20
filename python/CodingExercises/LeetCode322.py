'''
322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

import collections

def LeetCode322(coins, amt):

    fnl_lst=[]
    tmp=[]
    Combinations_recur(coins,fnl_lst,tmp,amt)

    if len(fnl_lst)>0:
        return sorted(fnl_lst,key=len)[0]
    else:
        return -1

def Combinations_recur(coins,fnl_lst,tmp,amt):

    if amt==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))

    for i in range(0,len(coins)):
        if coins[i]>amt:
            break
        tmp.append(coins[i])
        Combinations_recur(coins, fnl_lst, tmp, amt-coins[i])
        tmp.pop()

def main():

    coins=[1, 2, 5]
    amt=11
    print(LeetCode322(coins,amt))

    coins = [2]
    amt = 3
    print(LeetCode322(coins, amt))

if __name__=='__main__':
    main()