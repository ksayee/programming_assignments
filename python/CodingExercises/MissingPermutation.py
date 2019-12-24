'''
Missing Permutations in a list
Given a list of permutations of any word. Find the missing permutation from the list of permutations.
Examples:
Input : Permutation_given[] = {"ABCD", "CABD", "ACDB",
              "DACB", "BCDA", "ACBD", "ADCB", "CDAB",
              "DABC", "BCAD", "CADB", "CDBA", "CBAD",
              "ABDC", "ADBC", "BDCA", "DCBA", "BACD",
              "BADC", "BDAC", "CBDA", "DCAB"};
Output : DBAC DBCA
'''

import collections

def Combinations_recur(lst,cnt,tmp,fnl_lst,permutation):

    if len(tmp)==len(permutation[0]):
        if ''.join(tmp) not in permutation:
            fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst, permutation)
        tmp.pop()
        cnt[i]=cnt[i]+1

def MissingPermutation(permutation):

    dict=collections.Counter(permutation[0])
    lst=[]
    cnt=[]
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst,permutation)
    return fnl_lst

def main():

    permutation=["ABCD", "CABD", "ACDB",
              "DACB", "BCDA", "ACBD", "ADCB", "CDAB",
              "DABC", "BCAD", "CADB", "CDBA", "CBAD",
              "ABDC", "ADBC", "BDCA", "DCBA", "BACD",
              "BADC", "BDAC", "CBDA", "DCAB"]
    print(MissingPermutation(permutation))

if __name__=='__main__':
    main()