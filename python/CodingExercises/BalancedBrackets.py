# Check if the brackets in the given string in balanced or not.

def BalancedBrackets(str1):

    lst=list(str1)
    tmp=[]
    inside=False
    flg=True

    for i in range(0,len(lst)):
        inside=True
        key=lst[i]

        if key=='{' or key=='(' or key=='[' or key=='<':
            tmp.append(key)
        elif key=='}' or key==')' or key==']' or key=='>':
            if len(tmp)>0:
                if (key=='}' and tmp[-1]=='{') or (key=='>' and tmp[-1]=='<') or (key==')' and tmp[-1]=='(') or (key==']' and tmp[-1]=='['):
                    tmp.pop()
                else:
                    flg=False
                    break
            else:
                flg=False
                break
    if len(tmp)==0 and inside==False:
        return False
    elif len(tmp)>0 and flg==True:
        return False
    elif len(tmp)==0 and flg==True:
        return True
    elif flg==False:
        return False

def main():

    str1 = '({}[]()<>)'
    print(BalancedBrackets(str1))

    str1 = '(<[()]>)'
    print(BalancedBrackets(str1))

    str1 = ''
    print(BalancedBrackets(str1))

    str1 = '([]{{<>}()})'
    print(BalancedBrackets(str1))

    str1 = '((((((())'
    print(BalancedBrackets(str1))

    str1 = '()))'
    print(BalancedBrackets(str1))

    str1 = '(()()(()'
    print(BalancedBrackets(str1))

    str1 = ''
    print(BalancedBrackets(str1))

    str1 = 'This<might>not(be{balanced}'
    print(BalancedBrackets(str1))

    str1 = '{(<[SimpleExampleForBalanced]>)}'
    print(BalancedBrackets(str1))

    str1 = '{)(<[This]is>not)balanced}'
    print(BalancedBrackets(str1))

    str1 = '{(<[simple])>}'
    print(BalancedBrackets(str1))

    str1 = '{Another{Example<of>Unbalanced}String'
    print(BalancedBrackets(str1))

    str1 = '(This)is<how>balanced{string}with[paranthesis]canbe'
    print(BalancedBrackets(str1))

if __name__=='__main__':
    main()