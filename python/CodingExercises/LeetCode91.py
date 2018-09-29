'''
91. Decode Ways
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

import collections

def Validate_str(dict,lst):

    tmp=[]
    for l in lst:
        if int(l) not in dict.keys():
            tmp=[]
            break
        else:
            tmp.append(dict[int(l)])
    return ''.join(tmp)

def LeetCode91(dict,str1):

    lst=list(str1)

    tmp=[0]*(len(lst)*2)
    fnl_lst=[]

    idx=0
    op_idx=0
    Combinations_recur(lst,tmp,fnl_lst,idx,op_idx)
    out_lst=[]
    for s in fnl_lst:
        fnl_str=Validate_str(dict,s.split(','))
        if len(fnl_str)>0:
            tup=(fnl_str,s)
            out_lst.append(tup)
    return out_lst


def Combinations_recur(lst,tmp,fnl_lst,idx,op_idx):

    if idx==len(lst):
        fnl_lst.append(''.join(tmp).strip(','))
        return
    tmp[op_idx]=lst[idx]
    tmp[op_idx+1]=','
    Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+2)

    if idx+1<len(lst):
        Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+1)

def main():

    dict={}
    dict[1] = 'a'
    dict[2] = 'b'
    dict[3] = 'c'
    dict[4] = 'd'
    dict[5] = 'e'
    dict[6] = 'f'
    dict[7] = 'g'
    dict[8] = 'h'
    dict[9] ='i'
    dict[10] = 'j'
    dict[11] = 'k'
    dict[12] = 'l'
    dict[13] = 'm'
    dict[14] = 'n'
    dict[15] = 'o'
    dict[16] = 'p'
    dict[17] = 'q'
    dict[18] = 'r'
    dict[19] = 's'
    dict[20] = 't'
    dict[21] = 'u'
    dict[22] = 'v'
    dict[23] = 'w'
    dict[24] = 'x'
    dict[25] = 'y'
    dict[26] = 'z'

    str1='12'
    print(LeetCode91(dict,str1))

    str1 = '226'
    print(LeetCode91(dict, str1))

    str1 = '1234'
    print(LeetCode91(dict, str1))


if __name__=='__main__':
    main()