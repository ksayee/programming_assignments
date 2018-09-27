def Combinations_recur(fnl_lst,tmp,open,close,n):

    if n==close:
        fnl_lst.append(''.join(tmp.copy()))

    if open<n:
        tmp.append('{')
        Combinations_recur(fnl_lst, tmp, open+1, close, n)
        tmp.pop()
    if open>close:
        tmp.append('}')
        Combinations_recur(fnl_lst, tmp, open, close+1, n)
        tmp.pop()

def BalancedParenthesesCombinations(n):

    tmp=[]
    fnl_lst=[]

    Combinations_recur(fnl_lst,tmp,0,0,n)

    return fnl_lst

def main():

    n=2
    print(BalancedParenthesesCombinations(n))

    n = 3
    print(BalancedParenthesesCombinations(n))

    n = 5
    print(BalancedParenthesesCombinations(n))

if __name__=='__main__':
    main()