'''
242. Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''


def isAnagram(s, t):
    if ''.join(sorted(s)) == ''.join(sorted(t)):
        return True
    else:
        return False

def main():
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

    s = "rat"
    t = "car"
    print(isAnagram(s, t))

if __name__=='__main__':
    main()