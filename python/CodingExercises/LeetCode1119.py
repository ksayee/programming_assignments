'''
1119. Remove Vowels from a String
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:
Input: "aeiou"
Output: ""
Note:
S consists of lowercase English letters only.
1 <= S.length <= 1000
'''

def LeetCode1119(word):

    vowels=['a','e','i','o','u']
    fnl_lst=[]
    for letter in word:
        if letter in vowels:
            pass
        else:
            fnl_lst.append(letter)
    return ''.join(fnl_lst)

def main():

    word='leetcodeisacommunityforcoders'
    print(LeetCode1119(word))

    word = 'aeiou'
    print(LeetCode1119(word))

if __name__=='__main__':
    main()