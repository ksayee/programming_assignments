'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''


def LeetCode3(str1):

    lst=list(str1)

    curr_len=1
    max_len=1

    visited=[-1]*26
    key=lst[0]
    visited[ord(key)-ord('a')]=0

    for i in range(1,len(lst)):

        key=lst[i]
        prev_val=visited[ord(key)-ord('a')]

        if prev_val==-1 or i-curr_len>prev_val:
            curr_len=curr_len+1
        else:
            if curr_len>max_len:
                max_len=curr_len
            curr_len=i-prev_val

        visited[ord(key)-ord('a')]=i
    if curr_len>max_len:
        max_len=curr_len

    return max_len

def main():
    
    str1='abcabcbb'
    print(LeetCode3(str1))

    str1 = 'bbbbb'
    print(LeetCode3(str1))

    str1 = 'pwwkew'
    print(LeetCode3(str1))

if __name__=='__main__':
    main()