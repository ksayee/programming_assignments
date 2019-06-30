'''
692. Top K Frequent Words
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
'''

import collections
def LeetCode692(ary, k):
    dict=collections.Counter(ary)
    fnl_lst=[]
    dict_sort=sorted(dict.items(),key=lambda x:x[1],reverse=True)
    for i in range(0,k):
        fnl_lst.append(dict_sort[i][0])
    return fnl_lst

def main():

    ary=["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(LeetCode692(ary,k))

    ary = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(LeetCode692(ary, k))

if __name__=='__main__':
    main()