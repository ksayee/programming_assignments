'''
907. Sum of Subarray Minimums
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.
Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
'''

def LeetCode907(ary):

    lst=[]
    for i in range(0,len(ary)):
        lst.append(str(ary[i]))

    fnl_lst=[]
    tmp=[]
    Combinations_recur(''.join(lst),lst,fnl_lst,tmp)

    sum=0
    for key in fnl_lst:
        sum=sum+int(sorted(key)[0])
    return sum

def Combinations_recur(str1,lst,fnl_lst,tmp):

    if len(tmp)>0:

        try:
            cnt=str1.index(''.join(tmp))
        except:
            cnt=-1
        if cnt>=0:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(lst)):

        tmp.append(lst[i])
        Combinations_recur(str1,lst[i+1:], fnl_lst, tmp)
        tmp.pop()

def main():

    ary=[3,1,2,4]
    print(LeetCode907(ary))

if __name__=='__main__':
    main()