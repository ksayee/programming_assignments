'''
Minimum number of bracket reversals needed to make an expression balanced
Given an expression with only ‘}’ and ‘{‘. The expression may not be balanced. Find minimum number of bracket reversals to make the expression balanced.
Examples:

Input:  exp = "}{"
Output: 2
We need to change '}' to '{' and '{' to
'}' so that the expression becomes balanced,
the balanced expression is '{}'

Input:  exp = "{{{"
Output: Can't be made balanced using reversals

Input:  exp = "{{{{"
Output: 2

Input:  exp = "{{{{}}"
Output: 1

Input:  exp = "}{{}}{{{"
Output: 3
'''

def MinimumNumberBracketsReversal(str1):

    lst=list(str1)
    tmp=[]
    for key in lst:

        if key=='{':
            tmp.append(key)
        elif key=='}':
            if len(tmp)==0:
                tmp.append(key)
            elif tmp[-1]=='{':
                tmp.pop()
        else:
            tmp.append(key)

    if len(tmp)==0:
        return 0
    else:
        size=len(tmp)
        i=0
        open=0
        close=0
        while i<size:
            if tmp[i]=='{':
                open=open+1
            else:
                close=close+1
            i=i+1

        tmp=size/2 + close%2

        if tmp%1==0:
            return int(tmp)
        else:
            return -1

def main():

    str1='}{'
    print(MinimumNumberBracketsReversal(str1))

    str1 = '{{{'
    print(MinimumNumberBracketsReversal(str1))

    str1 = '{{{{'
    print(MinimumNumberBracketsReversal(str1))

    str1 = '{{{{}}'
    print(MinimumNumberBracketsReversal(str1))

    str1 = '}{{}}{{{'
    print(MinimumNumberBracketsReversal(str1))

if __name__=='__main__':
    main()