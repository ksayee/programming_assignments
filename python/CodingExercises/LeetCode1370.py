'''
1370. Increasing Decreasing String
Given a string s. You should re-order the string using the following algorithm:
Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
Return the result string after sorting s with this algorithm.
Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
Example 2:
Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
Example 3:
Input: s = "leetcode"
Output: "cdelotee"
Example 4:
Input: s = "ggggggg"
Output: "ggggggg"
Example 5:
Input: s = "spo"
Output: "ops"
'''

import collections
def LeetCode1370(str1):

    dict=collections.Counter(str1)
    output_lst=[]
    while len(dict)>0:
        lst = list(dict.keys())
        while len(lst)>0:
            min_element=min(lst)
            idx=lst.index(min_element)
            lst.pop(idx)
            output_lst.append(min_element)
            if dict[min_element]==1:
                del dict[min_element]
            else:
                dict[min_element]=dict[min_element]-1
        lst = list(dict.keys())
        while len(lst)>0:
            max_element=max(lst)
            idx=lst.index(max_element)
            lst.pop(idx)
            output_lst.append(max_element)
            if dict[max_element]==1:
                del dict[max_element]
            else:
                dict[max_element]=dict[max_element]-1
    return ''.join(output_lst)

def main():

    str1='aaaabbbbcccc'
    print(LeetCode1370(str1))

    str1 = 'rat'
    print(LeetCode1370(str1))

    str1 = 'leetcode'
    print(LeetCode1370(str1))

    str1 = 'ggggggg'
    print(LeetCode1370(str1))

    str1 = 'spo'
    print(LeetCode1370(str1))

if __name__=='__main__':
    main()