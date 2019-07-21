'''
279. Perfect Squares
Medium
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
which sum to n.
Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

import math
def CheckPerfectSquare(n):

    temp=math.sqrt(n)
    if str(temp).split('.')[1]=='0':
        return True
    else:
        return False

def Combinations_recur(perfect_square,tmp,fnl_lst,tgt):

    if tgt==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(sorted(tmp.copy()))
        return

    for i in range(0,len(perfect_square)):
        if tgt<0:
            break
        tmp.append(perfect_square[i])
        Combinations_recur(perfect_square, tmp, fnl_lst, tgt-perfect_square[i])
        tmp.pop()

def LeetCode279(num):

    perfect_square=[]

    i=1
    while i<num:
        flg=CheckPerfectSquare(i)
        if flg==True:
            perfect_square.append(i)
        i=i+1

    tmp=[]
    fnl_lst=[]
    tgt=num
    Combinations_recur(perfect_square,tmp,fnl_lst,tgt)
    return sorted(fnl_lst,key=lambda x:len(x))[0]

def main():

    num=12
    print(LeetCode279(num))

    num = 13
    print(LeetCode279(num))

if __name__=='__main__':
    main()