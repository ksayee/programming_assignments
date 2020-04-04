'''
1170. Compare Strings by Frequency of the Smallest Character
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.
Example 1:
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
'''

import collections
def FindFreq(word):

    letters_dict=collections.Counter(list(word))
    return sorted(letters_dict.items(),key=lambda x:x[0])[0][1]

def LeetCode1170(queries,words):
    wordsFreq={}
    for word in words:
        value=FindFreq(word)
        if value in wordsFreq.keys():
            wordsFreq[value].append(word)
        else:
            wordsFreq[value]=[]
            wordsFreq[value].append(word)

    output_lst=[]
    for query in queries:
        cnt=0
        value=FindFreq(query)
        for key,val in wordsFreq.items():
            if value<key:
                cnt=cnt+len(wordsFreq[key])
        output_lst.append(cnt)
    return output_lst

def main():

    queries = ["cbd"]
    words = ["zaaaz"]
    print(LeetCode1170(queries,words))

    queries = ["bbb","cc"]
    words = ["a","aa","aaa","aaaa"]
    print(LeetCode1170(queries, words))

if __name__=='__main__':
    main()