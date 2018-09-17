'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

def LeetCode125(str1):

    lst=[]

    for i in range(0,len(str1)):
        key=str1[i]
        if (key>='A' and key<='Z') or (key>='a' and key<='z'):
            lst.append(key.lower())

    l=0
    r=len(lst)-1

    flg=True
    while l<r:

        if lst[l]!=lst[r]:
            flg=False
            break
        else:
            l=l+1
            r=r-1

    return flg

def main():
    
    str1='A man, a plan, a canal: Panama'
    print(LeetCode125(str1))

    str1 = 'race a car'
    print(LeetCode125(str1))

if __name__=='__main__':
    main()