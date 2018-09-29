'''
243. Shortest Word Distance

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


def LeetCode243(words, word1, word2):

    dict={}

    for i in range(0,len(words)):
        key=words[i]

        if word1==key:

            if word1 in dict.keys():
                dict[word1].append(i)
            else:
                tmp=[]
                tmp.append(i)
                dict[word1]=tmp

        if word2 == key:

            if word2 in dict.keys():
                dict[word2].append(i)
            else:
                tmp = []
                tmp.append(i)
                dict[word2] = tmp

    val1=dict[word1]
    val2=dict[word2]

    min_dist=1000
    for l in val1:
        for r in val2:
            dist=abs(l-r)
            if dist<min_dist:
                min_dist=dist

    return min_dist

def main():

    word1='coding'
    word2='practice'
    words=["practice", "makes", "perfect", "coding", "makes"]
    print(LeetCode243(words,word1,word2))

    word1 = 'makes'
    word2 = 'coding'
    words = ["practice", "makes", "perfect", "coding", "makes"]
    print(LeetCode243(words, word1, word2))

if __name__=='__main__':
    main()