'''
709. To Lower Case
Easy
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
Example 1:
Input: "Hello"
Output: "hello"
Example 2:
Input: "here"
Output: "here"
Example 3:
Input: "LOVELY"
Output: "lovely"
'''

def LeetCode709(word):

    return word.lower()

def main():

    word='Hello'
    print(LeetCode709(word))

    word = 'here'
    print(LeetCode709(word))

    word = 'LOVELY'
    print(LeetCode709(word))

if __name__=='__main__':
    main()