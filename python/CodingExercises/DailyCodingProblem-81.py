'''
This problem was asked by Yelp.
Given a mapping of digits to letters (as in a phone number), and a digit string, return all
possible letters the number could represent. You can assume each valid number in the
mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], ...} then “23” should return [“ad”, “ae”, “af”,
“bd”, “be”, “bf”, “cd”, “ce”, “cf"].
'''

import collections
def DailyCodingProblem81(dict,str1):

    inp_lst=[]
    for i in range(0,len(str1)):
        key=int(str1[i])
        if key in dict.keys():
            inp_lst.append(dict[key])
    inp_dict=collections.Counter(''.join(inp_lst))

    lst=[]
    cnt=[]
    for key,val in inp_dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]

    Combinations_recur(str1,lst,cnt,tmp,fnl_lst)

    out_lst=[]

    for lst in fnl_lst:
        i=0
        flg=True
        for l in lst:
            key=str1[i]
            if l in dict[int(key)]:
                i=i+1
            else:
                flg=False
                break
        if flg==True:
            out_lst.append(''.join(lst))

    return out_lst

def Combinations_recur(str1,lst,cnt,tmp,fnl_lst):

    if len(tmp)==len(str1):
        fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(str1, lst, cnt, tmp, fnl_lst)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():

    dict={}
    dict[2] = 'abc'
    dict[3] = 'def'
    dict[4] = 'ghi'
    dict[5] = 'jkl'
    dict[6] = 'mno'
    dict[7] = 'pqrs'
    dict[8] = 'tuv'
    dict[9] = 'wxyz'

    str1='23'
    print(DailyCodingProblem81(dict,str1))

    str1 = '223'
    print(DailyCodingProblem81(dict, str1))

if __name__=='__main__':
    main()