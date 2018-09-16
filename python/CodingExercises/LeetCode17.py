'''
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

import collections

def LeetCode17(str1):

    dict={}

    dict[2]='abc'
    dict[3] = 'def'
    dict[4] = 'ghi'
    dict[5] = 'jkl'
    dict[6] = 'mno'
    dict[7] = 'pqrs'
    dict[8] = 'tuv'
    dict[9] = 'wxyz'

    src_lst=[]
    for i in range(0,len(str1)):
        key=int(str1[i])
        src_lst.append(dict[key])

    src_dict=collections.Counter(''.join(src_lst))

    lst=[]
    cnt=[]

    for key, val in src_dict.items():
        lst.append(key)
        cnt.append(val)

    res_lst=[]
    tmp=[]
    Combinations_recur(lst,cnt,res_lst,tmp)

    flg=True
    fnl_lst=[]
    for l in res_lst:

        if len(l)==len(str1):
            flg=True
            for i in range(0,len(l)):
                key=int(str1[i])
                val_lst=list(dict[key])
                if l[i] not in val_lst:
                    flg=False
            if flg==True:
                fnl_lst.append(''.join(l))

    return fnl_lst


def Combinations_recur(lst,cnt,res_lst,tmp):


    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        res_lst.append(tmp.copy())
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, res_lst, tmp)
        tmp.pop()
        cnt[i]=cnt[i]+1


def main():

    str1='23'
    print(LeetCode17(str1))

    str1 = '223'
    print(LeetCode17(str1))


if __name__=='__main__':
    main()