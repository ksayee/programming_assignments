'''
132. Palindrome Partitioning II
Hard
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

def Validate(word_str):

    lst=word_str.split(',')
    for sub_word in lst:
        if ''.join(reversed(sub_word))==sub_word:
            pass
        else:
            return False
    return True

def Combinations_recur(tmp,idx,op_idx,output_lst,word):

    if idx==len(word):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            output_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, output_lst, word)

    if idx+1<len(word):
        Combinations_recur(tmp, idx+1, op_idx+1, output_lst, word)

def LeetCode132(word):

    tmp=[0]*len(word)*2
    idx=0
    op_idx=0
    output_lst=[]
    Combinations_recur(tmp,idx,op_idx,output_lst,word)
    return sorted(output_lst,key=lambda x:len(x))[0]

def main():
    
    str1='aab'
    print(LeetCode132(str1))

    str1 = 'ababbbabbababa'
    print(LeetCode132(str1))

if __name__=='__main__':
    main()