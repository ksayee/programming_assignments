'''
Good morning! Here's your coding interview problem for today.
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''

import collections
def DailyCodingProblem22(ary,str1):

    lst=[]
    cnt=[]
    dict=collections.Counter(ary)
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,str1,tmp,fnl_lst)
    return fnl_lst

def Combinations_recur(lst,cnt,str1,tmp,fnl_lst):

    if len(''.join(tmp))==len(str1):
        if ''.join(tmp)==str1:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, str1, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()


def main():

    ary=['quick', 'brown', 'the', 'fox']
    str1='thequickbrownfox'
    print(DailyCodingProblem22(ary,str1))

    ary = ['bed', 'bath', 'bedbath', 'and', 'beyond']
    str1 = 'bedbathandbeyond'
    print(DailyCodingProblem22(ary, str1))
    
if __name__=='__main__':
    main()