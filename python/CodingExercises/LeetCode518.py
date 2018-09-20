'''
518. Coin Change 2
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
'''

import collections

def LeetCode518(coins, amt):

    fnl_lst=[]
    tmp=[]

    Combinations_recur(coins,fnl_lst,tmp,amt)

    return fnl_lst

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
    amt=5
    print(LeetCode518(coins,amt))

    coins = [2]
    amt = 3
    print(LeetCode518(coins, amt))

if __name__=='__main__':
    main()