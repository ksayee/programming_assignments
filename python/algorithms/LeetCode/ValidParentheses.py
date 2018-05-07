'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

def ValidParentheses(str):

    if len(str)==0:
        return None
    else:
        lst=[]


    for i in range(0,len(str)):
        if str[i]=='[' or str[i]=='{' or str[i]=='(':
            lst.append(str[i])
        elif str[i] == ']':
            if lst[-1]=='[':
                lst.pop()
            else:
                return False
        elif str[i] == ')':
            if lst[-1] == '(':
                lst.pop()
            else:
                return False
        elif str[i] == '}':
            if lst[-1] == '{':
                lst.pop()
            else:
                return False
    return True

def main():

    str='()'
    print(ValidParentheses(str))

    str = '()[]{}'
    print(ValidParentheses(str))

    str = '(]'
    print(ValidParentheses(str))

    str = '([)]'
    print(ValidParentheses(str))


if __name__=='__main__':
    main()
