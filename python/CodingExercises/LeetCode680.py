'''
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
'''

def LeetCode680(str1):

    lst=list(str1)

    tmp=[0]*26

    for i in range(0,len(lst)):
        key=lst[i]
        tmp[ord(key)-ord('a')]=tmp[ord(key)-ord('a')]+1

    cnt=0
    for i in range(0,len(tmp)):

        if tmp[i]%2==1:
            cnt=cnt+1

    if cnt-1>1:
        return False
    else:
        return True




def main():

    str1='aba'
    print(LeetCode680(str1))

    str1 = 'abca'
    print(LeetCode680(str1))

if __name__=='__main__':
    main()