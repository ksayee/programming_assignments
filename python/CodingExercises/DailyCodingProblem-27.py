'''
This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

def DailyCodingProblem27(str1):

    lst=list(str1)

    tmp=[]
    for i in range(0,len(lst)):

        key=lst[i]

        if key=='(' or key=='{' or key=='[':
            tmp.append(key)
        elif key==')' or key=='}' or key==']':
            if (tmp[-1]=='(' and key==')') or (tmp[-1]=='{' and key=='}') or (tmp[-1]=='[' and key==']'):
                tmp.pop()
            else:
                break

    if len(tmp)==0:
        return True
    else:
        return False

def main():

    str1='([])[]({})'
    print(DailyCodingProblem27(str1))

    str1 = '([)]'
    print(DailyCodingProblem27(str1))

    str1 = '((()'
    print(DailyCodingProblem27(str1))

    str1 = ''
    print(DailyCodingProblem27(str1))

if __name__=='__main__':
    main()