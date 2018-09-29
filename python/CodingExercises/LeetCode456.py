'''
456. 132 Pattern
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj.
Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''

def Validate_pattern(tmp,ptrn):

    lst=list(ptrn)

    flg=True

    for i in range(1,len(tmp)):

        if (tmp[i]>tmp[i-1] and lst[i]>lst[i-1]) or (tmp[i]<tmp[i-1] and lst[i]<lst[i-1]):
            continue
        else:
            flg=False
            break

    return flg

def LeetCode456(ary, ptrn):

    fnl_lst=[]
    tmp=[]

    Combinations_recur(ary,fnl_lst,tmp,ptrn)

    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,ptrn):

    if len(tmp) == len(ptrn):
        flg = Validate_pattern(tmp, ptrn)
        if flg == True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(ary)):
        tmp.append(ary[i])
        Combinations_recur(ary[i+1:], fnl_lst, tmp, ptrn)
        tmp.pop()

def main():

    ary=[1, 2, 3, 4]
    ptrn='132'
    print(LeetCode456(ary,ptrn))

    ary = [3, 1, 4, 2]
    ptrn = '132'
    print(LeetCode456(ary, ptrn))

    ary = [-1, 3, 2, 0]
    ptrn = '132'
    print(LeetCode456(ary, ptrn))

if __name__=='__main__':
    main()