'''
1221. Split a String in Balanced Strings
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.
Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
Example 4:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
'''

import collections
def Validate(chk_str):

    tmp_lst=chk_str.split(',')

    for element in tmp_lst:
        dict=collections.Counter(element)
        if len(dict.keys())==2 and dict['R']==dict['L']:
            pass
        else:
            return False
    return True


def Combinations_recur(lst,tmp,fnl_lst,idx,op_idx):

    if idx==len(lst):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            fnl_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=lst[idx]
    tmp[op_idx+1]=','
    Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+2)

    if idx+1<len(lst):
        Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+1)

def LeetCode1221(str1):

    lst=list(str1)
    tmp=[0]*(len(str1)*2)
    fnl_lst=[]
    idx=0
    op_idx=0
    Combinations_recur(lst,tmp,fnl_lst,idx,op_idx)
    return fnl_lst

def main():

    str1='RLRRLLRLRL'
    print(LeetCode1221(str1))

    str1 = 'RLLLLRRRLR'
    print(LeetCode1221(str1))

    str1 = 'LLLLRRRR'
    print(LeetCode1221(str1))

    str1 = 'RLRRRLLRLL'
    print(LeetCode1221(str1))

if __name__=='__main__':
    main()