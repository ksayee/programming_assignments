'''
Print all permutations with repetition of characters
Given a string of length n, print all permutation of the given string. Repetition of characters is allowed. Print these permutations in lexicographically sorted order
Examples:

Input: AB
Ouput: All permutations of AB with repetition are:
      AA
      AB
      BA
      BB

Input: ABC
Output: All permutations of ABC with repetition are:
       AAA
       AAB
       AAC
       ABA
       ...
       ...
       CCB
       CCC
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst,str1):

    if len(tmp)==len(str1):
        if ''.join(tmp) not in fnl_lst:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst,str1)
        cnt[i]=cnt[i]+1
        tmp.pop()

def PermutationsWithRepetitionCharacters(str1):

    dict={}
    for i in range(0,len(str1)):
        letter=str1[i]
        dict[letter]=len(str1)

    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,str1)
    return fnl_lst

def main():
    
    str1='AB'
    print(PermutationsWithRepetitionCharacters(str1))

    str1 = 'ABC'
    print(PermutationsWithRepetitionCharacters(str1))

if __name__=='__main__':
    main()