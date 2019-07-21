'''
583. Delete Operation for Two Strings
Medium
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same,
where in each step you can delete one character in either string.
Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
'''

import collections
def LeetCode583(word1,word2):

    dict=collections.Counter(word1)

    for key in word2:
        if key in dict.keys():
            dict[key]=dict.get(key)-1
        else:
            dict[key]=1

    cnt=0
    for key,val in dict.items():
        if val>0:
            cnt=cnt+val
        else:
            cnt=cnt+(-1*val)
    return cnt

def main():

    word1="sea"
    word2="eat"
    print(LeetCode583(word1,word2))

if __name__=='__main__':
    main()