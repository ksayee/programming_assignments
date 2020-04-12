'''
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.
Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

def CheckPalindrome(element):

    if len(element)==1:
        return True
    i=0
    j=len(element)-1
    while i<j:
        if element[i]!=element[j]:
            return False
        i=i+1
        j=j-1
    return True

def Validate(tmp_str):

    tmp_lst=tmp_str.split(',')

    for element in tmp_lst:
        flg=CheckPalindrome(element)
        if flg==False:
            return False
    return True

def Combinations_recur(lst,tmp,fnl_lst,idx,op_idx):

    if idx==len(lst):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            fnl_lst.append(''.join(tmp).strip(',').split(','))
        return
    tmp[op_idx]=lst[idx]
    tmp[op_idx+1]=','
    Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+2)
    if idx+1<len(lst):
        Combinations_recur(lst, tmp, fnl_lst, idx+1, op_idx+1)
        
def LeetCode131(str1):

    tmp=['0']*len(str1)*2
    idx=0
    op_idx=0
    lst=list(str1)
    fnl_lst=[]
    Combinations_recur(lst,tmp,fnl_lst,idx,op_idx)
    return fnl_lst

def main():

    str1='aab'
    print(LeetCode131(str1))

if __name__=='__main__':
    main()