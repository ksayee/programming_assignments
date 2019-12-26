'''
Longest common anagram subsequence from N strings
Given N strings. Find the longest possible subsequence from each of these N strings such that they are anagram to each other.
The task is to print the lexicographically largest subsequence among all the subsequences.
Examples:
Input: s[] = { geeks, esrka, efrsk }
Output: ske
First string has “eks”, Second string has “esk”, third string has “esk”. These three are anagrams. “ske” is lexoigrapically large.
Input: string s[] = { loop, lol, olive }
Output: ol
'''

def LongestCommonAnagramSequenceNStrings(ary):

    lst=[[0 for x in range(0,25)] for y in range(0,len(ary))]

    for i in range(0,len(ary)):
        word=ary[i]
        for letter in word:
            lst[i][ord(letter)-ord('a')]=lst[i][ord(letter)-ord('a')]+1

    output_list=[]
    for i in range(0,25):
        min=99999
        for j in range(0,len(ary)):
            if lst[j][i]<min:
                min=lst[j][i]
        while min>0:
            output_list.append(chr(ord('a')+i))
            min=min-1
    return ''.join(sorted(output_list,reverse=True))

def main():

    ary=['geeks', 'esrka', 'efrsk']
    print(LongestCommonAnagramSequenceNStrings(ary))

    ary = ['loop', 'lol', 'olive']
    print(LongestCommonAnagramSequenceNStrings(ary))

if __name__=='__main__':
    main()