'''
389. Find the Difference

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''


def findTheDifference(s, t):
    lst = [0] * 26

    for i in range(0, len(s)):
        c = s[i]
        lst[ord(c) - 97] = lst[ord(c) - 97] + 1
    for i in range(0, len(t)):
        c = t[i]
        lst[ord(c) - 97] = lst[ord(c) - 97] - 1
        if lst[ord(c) - 97] < 0:
            return c

def main():
    s = "abcd"
    t = "abcde"
    print(findTheDifference(s, t))

if __name__=='__main__':
    main()