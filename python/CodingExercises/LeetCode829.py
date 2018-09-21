'''
829. Consecutive Numbers Sum
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
'''

def Validate_list(tmp):

    lst=sorted(tmp)

    flg=True
    for i in range(1,len(lst)):
        if lst[i]-lst[i-1]>1:
            flg=False
            break

    return flg

def LeetCode829(n):

    ary=[]

    i=1
    while i<=int(n/2)+1:
        ary.append(i)
        i=i+1
    fnl_lst=[]
    tmp=[]
    sum=n

    Combinations_recur(ary,fnl_lst,tmp,sum)

    return fnl_lst

def Combinations_recur(ary,fnl_lst,tmp,sum):

    if sum==0:
        flg=Validate_list(tmp)
        if flg==True:
            fnl_lst.append(tmp.copy())

    for i in range(0,len(ary)):
        if sum<0:
            break
        tmp.append(ary[i])
        Combinations_recur(ary[i+1:], fnl_lst, tmp, sum-ary[i])
        tmp.pop()


def main():

    n = 5
    print(LeetCode829(n))

    n = 9
    print(LeetCode829(n))

    n = 15
    print(LeetCode829(n))

if __name__=='__main__':
    main()