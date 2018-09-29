'''
856. Score of Parentheses
Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
'''

def LeetCode856(str1):

    tmp=[]

    for i in range(0,len(str1)):
        key=str1[i]

        if key==')':
            if tmp[-1]=='(':
                tmp.pop()
                tmp.append(str(1))
            elif (tmp[-1]>='1' and tmp[-1]<='9') and (tmp[-2]>='1' and tmp[-2]<='9'):
                n1=tmp.pop()
                n2=tmp.pop()
                tmp.pop()
                tmp.append(str(2*(int(n1)+int(n2))))
            elif (tmp[-1]>='1' and tmp[-1]<='9'):
                n=tmp.pop()
                tmp.pop()
                tmp.append(str(2*int(n)))
        else:
            tmp.append(key)

    sum=0
    for l in tmp:
        sum=sum+int(l)
    return sum


def main():

    str1='()'
    print(LeetCode856(str1))

    str1 = '(())'
    print(LeetCode856(str1))

    str1 = '()()'
    print(LeetCode856(str1))

    str1 = '(()(()))'
    print(LeetCode856(str1))

if __name__=='__main__':
    main()