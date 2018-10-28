'''
306. Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199.
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
'''

def LeetCode306(n):

    str1=str(n)

    lst=['0']*(len(str1)*2)

    idx=0
    op_idx=0
    fnl_lst=[]
    Combinations_recur(lst,idx,op_idx,fnl_lst,str1)

    out_lst=[]

    for key in fnl_lst:
        tmp=key.split(',')
        flg=True
        for i in range(2,len(tmp)):
            if int(tmp[i-2])+int(tmp[i-1])==int(tmp[i]):
                continue
            else:
                flg=False
                break
        if flg==True:
            for l in tmp:
                out_lst.append(int(l))
            break

    return out_lst

def Combinations_recur(lst,idx,op_idx,fnl_lst,str1):

    if idx==len(str1):
        fnl_lst.append(''.join(lst).strip(','))
        return

    lst[op_idx]=str1[idx]
    lst[op_idx+1]=','
    Combinations_recur(lst, idx+1, op_idx+2, fnl_lst, str1)

    if idx+1<len(str1):
        Combinations_recur(lst, idx+1, op_idx+1, fnl_lst, str1)

def main():

    n=112358
    print(LeetCode306(n))

    n = 199100199
    print(LeetCode306(n))

if __name__=='__main__':
    main()