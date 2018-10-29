'''
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.
Example 1:
Input: "hello"
Output: "holle"
Example 2:
Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


def LeetCode345(str1):

    lst=list(str1)

    i=0
    j=len(lst)-1

    vow=['a','e','i','o','u']

    while i<j:

        if lst[i] in vow and lst[j] in vow:
            tmp=lst[i]
            lst[i]=lst[j]
            lst[j]=tmp
            i=i+1
            j=j-1
        else:
            if lst[i] not in vow:
                i=i+1
            if lst[j] not in vow:
                j=j-1
    return ''.join(lst)

def main():

    str1 = "hello"
    print(LeetCode345(str1))

    str1 = "leetcode"
    print(LeetCode345(str1))

if __name__=='__main__':
    main()