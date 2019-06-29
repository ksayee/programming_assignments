'''
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

def Validate(key,wordDict):
    flg=True
    tmp1=key.split(',')
    for l in tmp1:
        if l not in wordDict:
            flg=False
            break
    return flg

def LeetCode139(str1,wordDict):

    lst=list(str1)
    tmp=[0]*(len(str1)*2)

    fnl_lst=[]
    idx=0
    op_idx=0
    Combinations_recur(lst,tmp,idx,op_idx,fnl_lst,wordDict)
    if len(fnl_lst)==0:
        return False
    else:
        return True

def Combinations_recur(lst,tmp,idx,op_idx,fnl_lst,wordDict):

    if idx==len(lst):
        flg=Validate(''.join(tmp).strip(','),wordDict)
        if flg==True:
            fnl_lst.append(''.join(tmp).strip(','))
        return

    tmp[op_idx]=lst[idx]
    tmp[op_idx+1]=','
    Combinations_recur(lst, tmp, idx+1, op_idx+2, fnl_lst,wordDict)

    if idx+1<len(lst):
        Combinations_recur(lst, tmp, idx+1, op_idx+1, fnl_lst,wordDict)

def main():

    str1='leetcode'
    wordDict = ["leet", "code"]
    print(LeetCode139(str1,wordDict))

    str1 = 'applepenapple'
    wordDict = ["apple", "pen"]
    print(LeetCode139(str1, wordDict))

    str1 = 'catsandog'
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(LeetCode139(str1, wordDict))

if __name__=='__main__':
    main()