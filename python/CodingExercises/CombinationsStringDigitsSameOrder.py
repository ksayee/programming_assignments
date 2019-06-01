'''
Combinations in a String of Digits
Given an input string of numbers, find all combinations of numbers that can be formed using digits in the same order.

Examples:

Input : 123
Output :1 2 3
        1 23
        12 3
        123

Input : 1234
Output : 1 2 3 4
        1 2 34
        1 23 4
        1 234
        12 3 4
        12 34
        123 4
        1234
'''

def combinations_recur(lst,tmp,fnl_lst,idx,out):

    if idx==len(lst):
        fnl_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[out]=lst[idx]
    tmp[out+1]=','
    combinations_recur(lst, tmp, fnl_lst, idx+1,out+2)
    if idx+1<len(lst):
        combinations_recur(lst, tmp, fnl_lst, idx+1,out+1 )

def CombinationsStringDigitsSameOrder(str1):

    lst=list(str1)
    tmp=['@']*len(lst)*2
    fnl_lst=[]
    idx=0
    out=0
    combinations_recur(lst,tmp,fnl_lst,idx,out)
    return fnl_lst

def main():

    str1='123'
    print(CombinationsStringDigitsSameOrder(str1))

    str1 = '1234'
    print(CombinationsStringDigitsSameOrder(str1))

if __name__=='__main__':
    main()