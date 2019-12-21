'''
This problem was asked by WeWork.
You are given an array of integers representing coin denominations and a total amount of money.
Write a function to compute the fewest number of coins needed to make up that amount.
If it is not possible to make that amount, return null.
For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.
Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.
'''

def Combinations_recur(ary,tmp,fnl_lst,target):

    if target==0:
        if sorted(tmp) not in fnl_lst:
            fnl_lst.append(tmp.copy())
        return

    for i in range(0,len(ary)):
        if len(fnl_lst)>0:
            break
        if ary[i]>target:
            break
        tmp.append(ary[i])
        Combinations_recur(ary, tmp, fnl_lst, target-ary[i])
        tmp.pop()

def DailyCodingProblem384(ary,k):

    tmp=[]
    fnl_lst=[]
    ary=sorted(ary,reverse=True)
    print(ary)
    Combinations_recur(ary,tmp,fnl_lst,k)
    print(fnl_lst)
    return sorted(fnl_lst,key=lambda x:len(x))[0]

def main():

    ary=[1, 5, 10]
    k=56
    print(DailyCodingProblem384(ary,k))

    ary = [5, 8]
    k = 15
    print(DailyCodingProblem384(ary, k))

if __name__=='__main__':
    main()