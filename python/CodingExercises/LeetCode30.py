'''
30. Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []
'''

import collections
def LeetCode30(str1, words):

    dict=collections.Counter(words)

    lst=[]
    cnt=[]

    for key,val in dict.items():
        lst.append(key)
        cnt.append(val)

    tmp=[]
    res_lst=[]
    fnl_lst=[]
    Combinations_recur(lst,cnt,tmp,res_lst,words)

    for l in res_lst:
        key=''.join(l)
        try:
            idx=str1.index(key)
        except:
            continue
        fnl_lst.append(idx)
    return fnl_lst

def Combinations_recur(lst,cnt,tmp,res_lst,words):

    if len(tmp)==len(words):
        res_lst.append(tmp.copy())

    for i in range(0,len(lst)):
        if cnt[i]==0:
            continue
        tmp.append(lst[i])
        cnt[i]=cnt[i]-1
        Combinations_recur(lst, cnt, tmp,res_lst, words)
        tmp.pop()
        cnt[i]=cnt[i]+1

def main():
    
    str1='barfoothefoobarman'
    words = ["foo", "bar"]
    print(LeetCode30(str1,words))

    str1 = 'wordgoodstudentgoodword'
    words = ["word","student"]
    print(LeetCode30(str1, words))

if __name__=='__main__':
    main()