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
        if ary[i]>target:
            break
        tmp.append(ary[i])
        Combinations_recur(ary, tmp, fnl_lst, target-ary[i])
        tmp.pop()

def DailyCodingProblem384(ary,k):

    tmp=[]
    fnl_lst=[]
    Combinations_recur(ary,tmp,fnl_lst,k)
    return sorted(fnl_lst,key=lambda x:len(x))[0]

def DailyCodingProblem384_DP(ary, k):

    cache=[]
    for i in range(0,k+1):
        cache.append(float('inf'))

    for element in ary:
        if element<len(cache):
            cache[element]=1

    for i in range(1,k+1):
        if i-element>=0:
            lst=[]
            for d in ary:
                lst.append(cache[i-d])
            cache[i]=min(lst)+1

    if cache[k]==float('inf'):
        return 'NONE'
    return cache[k]

def main():

    ary=[1, 5, 10]
    k=56
    print(DailyCodingProblem384(ary,k))
    print(DailyCodingProblem384_DP(ary, k))

    ary = [5, 8]
    k = 15
    print(DailyCodingProblem384(ary, k))
    print(DailyCodingProblem384_DP(ary, k))

if __name__=='__main__':
    main()