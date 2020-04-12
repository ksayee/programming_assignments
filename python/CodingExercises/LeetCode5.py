'''
5. Longest Palindromic Substring
Medium
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: "cbbd"
Output: "bb"
'''

def Validate(lst_word,output_lst):
    lst=lst_word.split(',')

    for item in lst:
        if ''.join(reversed(item))==item:
            if len(item) in output_lst.keys():
                if item not in output_lst[len(item)]:
                    output_lst[len(item)].append(item)
            else:
                output_lst[len(item)]=[]
                output_lst[len(item)].append(item)

def Combinations_recur(tmp,idx,op_idx,output_lst,word):

    if idx==len(word):
        Validate(''.join(tmp).strip(','),output_lst)
        return

    tmp[op_idx]=word[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, idx+1, op_idx+2, output_lst,word)

    if idx+1<len(word):
        Combinations_recur(tmp, idx+1, op_idx+1, output_lst,word)

def LeetCode5(word):

    tmp=[0]*len(word)*2

    idx=0
    op_idx=0
    output_lst={}
    Combinations_recur(tmp,idx,op_idx,output_lst,word)
    return sorted(output_lst.items(),key=lambda x:x[0],reverse=True)[0][1]

def LeetCode5_DynamicProgram(str1):

    matrix=[['' for i in range(0,len(str1))] for j in range(0,len(str1))]

    for i in range(0,len(str1)):
        matrix[i][i]=str1[i]

    for k in range(2,len(str1)+1):
        for i in range(0,len(str1)-k+1):
            j=i+k-1
            if str1[i]==str1[j]:
                matrix[i][j]=str1[i:j+1]
            else:
                if len(matrix[i+1][j])>len(matrix[i][j-1]):
                    matrix[i][j]=matrix[i+1][j]
                else:
                    matrix[i][j] = matrix[i][j-1]

    for row in matrix:
        print(row)

    return matrix[0][-1]

def main():

    str1='babad'
    print(LeetCode5(str1))
    print(LeetCode5_DynamicProgram(str1))

    str1 = 'cbbd'
    print(LeetCode5(str1))
    print(LeetCode5_DynamicProgram(str1))

if __name__=='__main__':
    main()