'''
1163. Last Substring in Lexicographical Order
Given a string s, return the last substring of s in lexicographical order.
Example 1:
Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:
Input: "leetcode"
Output: "tcode"
'''

def Conbinations_recur(idx,op_idx,tmp,fnl_lst,str1):

    if idx==len(str1):
        fnl_lst.extend(set(''.join(tmp).strip(',').split(',')))
        return
    tmp[op_idx]=str1[idx]
    tmp[op_idx+1]=','
    Conbinations_recur(idx+1, op_idx+2, tmp, fnl_lst, str1)

    if idx+1<len(str1):
        Conbinations_recur(idx + 1, op_idx + 1, tmp, fnl_lst, str1)

def LeetCode1163(str1):

    tmp=['0']*2*len(str1)
    fnl_lst=[]
    Conbinations_recur(0,0,tmp,fnl_lst,str1)
    return sorted(set(fnl_lst))[-1]

def main():

    str1='abab'
    print(LeetCode1163(str1))

    str1 = 'leetcode'
    print(LeetCode1163(str1))

if __name__=='__main__':
    main()