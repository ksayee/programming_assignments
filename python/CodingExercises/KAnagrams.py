# Check if two strings are k-anagrams or not
# Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.
# Two strings are called k-anagrams if following two conditions are true.
# Both have same number of characters.
# Two strings can become anagram by changing at most k characters in a string.

def KAnagrams(str1,str2,k):

    lst=[0]*26

    for i in range(0,len(str1)):
        key=str1[i]
        lst[ord(key)-ord('a')]=lst[ord(key)-ord('a')]+1

    for i in range(0, len(str2)):
        key = str2[i]
        lst[ord(key) - ord('a')] = lst[ord(key) - ord('a')] - 1

    cnt=0
    for i in range(0,len(lst)):
        if lst[i]>0:
            cnt=cnt+lst[i]

    if cnt<=k:
        return True
    else:
        return False

def main():

    str1='anagram'
    str2='grammar'
    k=3
    print(KAnagrams(str1,str2,k))

    str1 = 'geeks'
    str2 = 'eggkf'
    k = 1
    print(KAnagrams(str1, str2, k))

if __name__=='__main__':
    main()