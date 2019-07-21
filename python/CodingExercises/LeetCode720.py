'''
720. Longest Word in Dictionary
Easy
Given a list of strings words representing an English Dictionary,
find the longest word in words that can be built one character at a time by other words in words.
 If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
'''

import collections

def LeetCode720(words):

    dict={}
    for word in words:
        if word not in dict.keys():
            dict[word]=[]

    for key in dict.keys():
        for word in words:
            if key==word:
                pass
            else:
                if key.startswith(word)==True:
                    dict[key].append(word)

    sort_dict=sorted(dict.items(),key=lambda x:(x[1],x[0]),reverse=True)
    return sort_dict[0]


def main():

    words = ["w", "wo", "wor", "worl", "world"]
    print(LeetCode720(words))

    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(LeetCode720(words))

if __name__=='__main__':
    main()