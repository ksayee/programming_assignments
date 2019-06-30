'''
819. Most Common Word
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
Words in the list of banned words are given in lowercase, and free of punctuation.
Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
'''

import collections
def LeetCode819(paragraph,banned):

    new_paragrah=paragraph.lower().replace(',','').replace('.','')

    dict=collections.Counter(new_paragrah.split(' '))
    lst=[]
    for key,val in dict.items():
        if key in banned:
            pass
        else:
            tup=(key,val)
            lst.append(tup)
    return sorted(lst,key=lambda x:x[1],reverse=True)[0][0]

def main():

    paragraph="Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(LeetCode819(paragraph,banned))

if __name__=='__main__':
    main()