'''
Print all ways to break a string in bracket form
Given a string, find all ways to to break the given string in bracket form. Enclose each substring within a parenthesis.

Examples:

Input : abc
Output: (a)(b)(c)
        (a)(bc)
        (ab)(c)
        (abc)


Input : abcd
Output : (a)(b)(c)(d)
         (a)(b)(cd)
         (a)(bc)(d)
         (a)(bcd)
         (ab)(c)(d)
         (ab)(cd)
         (abc)(d)
         (abcd)
'''

def PermutationsBreakStringBalancedForm(str1):

    lst=list(str1)
    tmp=['@']*len(lst)*2
    fnl_lst=[]
    idx=0
    out=0

    Combinations_recur(lst,tmp,fnl_lst,idx,out)

    print('Input String: ',''.join(lst))
    for int_lst in fnl_lst:
        print_lst=[]
        for key in int_lst:
            print_lst.append('(')
            print_lst.append(key)
            print_lst.append(')')
        print(''.join(print_lst))

def Combinations_recur(lst,tmp,fnl_lst,idx,out):

    if idx==len(lst):
        fnl_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[out]=lst[idx]
    tmp[out+1]=','
    Combinations_recur(lst, tmp, fnl_lst, idx+1, out+2)

    if idx+1<len(lst):
        Combinations_recur(lst, tmp, fnl_lst, idx+1, out+1)
    
def main():

    str1='abc'
    PermutationsBreakStringBalancedForm(str1)

    str1 = 'abcd'
    PermutationsBreakStringBalancedForm(str1)

if __name__=='__main__':
    main()