'''
140. Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
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

def LeetCode140(str1,wordDict):

    lst=list(str1)
    tmp=[0]*(len(str1)*2)
    fnl_lst=[]
    idx=0
    op_idx=0
    Combinations_recur(lst,tmp,idx,op_idx,fnl_lst,wordDict)
    return fnl_lst

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

    str1='catsanddog'
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(LeetCode140(str1,wordDict))

    str1 = 'pineapplepenapple'
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(LeetCode140(str1, wordDict))

if __name__=='__main__':
    main()