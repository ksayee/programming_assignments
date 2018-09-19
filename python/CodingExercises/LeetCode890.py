'''
890. Find and Replace Pattern

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
'''

import collections

def Return_Dict(itm):

    dict=collections.Counter(itm)

    lst=[]
    for i in range(0,len(itm)):
        key=itm[i]
        lst.append(str(dict[key]))

    return ''.join(lst)

def LeetCode890(ary,ptrn):

    fnl_lst=[]
    for key in ary:

        if Return_Dict(key)==Return_Dict(ptrn):
            fnl_lst.append(key)

    return fnl_lst

def main():
    
    ary=["abc","deq","mee","aqq","dkd","ccc"]
    ptrn="abb"
    print(LeetCode890(ary,ptrn))

if __name__=='__main__':
    main()