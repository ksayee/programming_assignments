'''
842. Split Array into Fibonacci Sequence
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.
Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.
Example 1:
Input: "123456579"
Output: [123,456,579]
Example 2:
Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:
Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:
Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:
Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
'''

def Validate(str2):

    lst=str2.split(',')

    if len(lst)<3:
        return False
    for i in range(2,len(lst)):
        if (len(lst[i-2])>1 and lst[i-2][0]=='0') or (len(lst[i-1])>1 and lst[i-1][0]=='0') or (len(lst[i])>1 and lst[i][0]=='0'):
            return False
        if int(lst[i-2])+int(lst[i-1])==int(lst[i]):
            continue
        else:
            return False
    return True

def Combinations_recur(tmp,fnl_lst,idx,op_idx,str1):

    if idx==len(str1):
        flg=Validate(''.join(tmp).strip(','))
        if flg==True:
            fnl_lst.append(''.join(tmp).strip(',').split(','))
        return

    tmp[op_idx]=str1[idx]
    tmp[op_idx+1]=','
    Combinations_recur(tmp, fnl_lst, idx+1, op_idx+2, str1)

    if idx+1<len(str1):
        Combinations_recur(tmp, fnl_lst, idx+1, op_idx+1, str1)
def LeetCode842(str1):

    tmp=['x']*len(str1)*2
    idx=0
    op_idx=0
    fnl_lst=[]
    Combinations_recur(tmp,fnl_lst,idx,op_idx,str1)
    return fnl_lst

def main():

    str1='123456579'
    print(LeetCode842(str1))

    str1 = '11235813'
    print(LeetCode842(str1))

    str1 = '112358130'
    print(LeetCode842(str1))

    str1 = '0123'
    print(LeetCode842(str1))

    str1 = '1101111'
    print(LeetCode842(str1))

if __name__=='__main__':
    main()