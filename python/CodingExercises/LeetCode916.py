'''
916. Word Subsets
We are given two arrays A and B of words.  Each word is a string of lowercase letters.
Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a.
Return a list of all universal words in A.  You can return the words in any order.
Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]
'''

import collections
def LeetCode916(A,B):

    fnl_lst=[]
    for word in A:
        dict=collections.Counter(word)
        flg=True
        for key in B:
            tmp_dict=collections.Counter(key)
            for key,val in tmp_dict.items():
                if key in dict.keys() and val<=dict[key]:
                    pass
                else:
                    flg=False
                    break
            if flg==False:
                break
        if flg==True:
            fnl_lst.append(word)
    return fnl_lst

def main():

    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]
    print(LeetCode916(A,B))

    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["l","e"]
    print(LeetCode916(A, B))

    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["e","oo"]
    print(LeetCode916(A, B))

    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["lo","eo"]
    print(LeetCode916(A, B))

    A = ["amazon","apple","facebook","google","leetcode"]
    B = ["ec","oc","ceo"]
    print(LeetCode916(A, B))

if __name__=='__main__':
    main()