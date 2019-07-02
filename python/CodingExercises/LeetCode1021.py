'''
1021. Remove Outermost Parentheses
Easy
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
 For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.
Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
'''

def LeetCode1021(str1):

    lst=list(str1)
    prev=0
    cnt=0
    fnl_lst=[]
    for i in range(0,len(lst)):
        if lst[i]=='(':
            cnt=cnt+1
        elif lst[i]==')':
            cnt=cnt-1
        if cnt==0:
            fnl_lst.append(''.join(lst[prev+1:i]))
            prev=i+1
    return ''.join(fnl_lst)

def main():

    str1="(()())(())"
    print(LeetCode1021(str1))

    str1 = "(()())(())(()(()))"
    print(LeetCode1021(str1))

    str1 = "()()"
    print(LeetCode1021(str1))

if __name__=='__main__':
    main()