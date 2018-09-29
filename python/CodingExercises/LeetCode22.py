'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def LeetCode22(n):

    tmp=[]
    fnl_lst=[]
    open=0
    close=0
    Combinations_recur(tmp,fnl_lst,open,close,n)

    return fnl_lst

def Combinations_recur(tmp,fnl_lst,open,close,n):

    if close==n:
        fnl_lst.append(''.join(tmp))
        return

    if open<n:
        tmp.append('{')
        Combinations_recur(tmp, fnl_lst, open+1, close, n)
        tmp.pop()
    if open>close:
        tmp.append('}')
        Combinations_recur(tmp, fnl_lst, open, close+1, n)
        tmp.pop()

def main():

    n=2
    print(LeetCode22(n))

    n=3
    print(LeetCode22(n))

    n=5
    print(LeetCode22(n))

if __name__=='__main__':
    main()