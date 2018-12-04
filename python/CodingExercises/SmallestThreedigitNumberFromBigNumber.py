# Check if both halves of the string have same set of characters in Python
# Given a string of lowercase characters only, the task is to check if it is possible to split a string from middle which will gives two halves having the same characters and same frequency of each character. If the length of the given string is ODD then ignore the middle element and check for the rest.

import collections
def SmallestThreeDigitNumberFromBigNumber(num):

    ary=list(str(num))
    lst=[]
    cnt=[]
    dict=collections.Counter(ary)
    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)
    tmp=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,fnl_lst)
    return sorted(fnl_lst)[0]

def Combinations_recur(lst,cnt,tmp,fnl_lst):

    if len(tmp)==3:
        fnl_lst.append(''.join(tmp))
        return

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp, fnl_lst)
        cnt[i]=cnt[i]+1
        tmp.pop()

def main():

    num=457801262
    print(SmallestThreeDigitNumberFromBigNumber(num))

if __name__=='__main__':
    main()