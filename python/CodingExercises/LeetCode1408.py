'''
1408. String Matching in an Array
Given an array of string words. Return all strings in words which is substring of another word in any order.
String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].
Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:
Input: words = ["blue","green","bu"]
Output: []
'''

def LeetCode1408(words):

    output_lst=[]

    for i in range(0,len(words)):
        for j in range(0,len(words)):
            if words[i]!=words[j]:
                try:
                    idx=words[j].index(words[i])
                    if words[i] not in output_lst:
                        output_lst.append(words[i])
                except:
                    pass
    return output_lst

def main():

    words = ["mass", "as", "hero", "superhero"]
    print(LeetCode1408(words))

    words = ["leetcode","et","code"]
    print(LeetCode1408(words))

    words = ["blue","green","bu"]
    print(LeetCode1408(words))

if __name__=='__main__':
    main()