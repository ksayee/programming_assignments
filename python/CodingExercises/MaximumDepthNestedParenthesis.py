'''
Find maximum depth of nested parenthesis in a string
We are given a string having parenthesis like below
     “( ((X)) (((Y))) )”
We need to find the maximum depth of balanced parenthesis, like 4 in above example. Since ‘Y’ is surrounded by 4 balanced parenthesis.
If parenthesis are unbalanced then return -1.

Examples :

Input : S = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)";
Output : 4

Input : S = "( p((q)) ((s)t) )";
Output : 3

Input : S = "";
Output : 0

Input : S = "b) (c) ()";
Output : -1

Input : S = "(b) ((c) ()"
Output : -1
'''

def MaximumDepthNestedParenthesis(str1):

    lst=[]
    max=0
    curr=0

    if len(str1)>0:
        for key in list(str1):
            if key=='(':
                lst.append('(')
                curr=curr+1

                if curr>max:
                    max=curr
            elif key==')':

                if curr>0:
                    curr=curr-1
                    lst.pop()
                else:
                    max=-1
                    break
    else:
        max=0

    if len(lst)!=0:
        max=-1
    return max

def main():

    str1='( a(b) (c) (d(e(f)g)h) I (j(k)l)m)'
    print(MaximumDepthNestedParenthesis(str1))

    str1 = '( p((q)) ((s)t) )'
    print(MaximumDepthNestedParenthesis(str1))

    str1 = ''
    print(MaximumDepthNestedParenthesis(str1))

    str1 = 'b) (c) ()'
    print(MaximumDepthNestedParenthesis(str1))

    str1 = '(b) ((c) ()'
    print(MaximumDepthNestedParenthesis(str1))

if __name__=='__main__':
    main()