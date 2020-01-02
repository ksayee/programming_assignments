'''
This is your coding interview problem for today.
This problem was asked by Facebook.
Given an array of numbers representing the stock prices of a company in chronological
order and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.
For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''

def DailyCodingProblem408(ary,k):

    profit=0
    buy=-1
    sell=-1
    i=1
    tmp=[]
    while i<len(ary):
        while i<len(ary) and ary[i]<ary[i-1]:
            i=i+1
        if i==len(ary):
            break
        buy=i-1
        while i<len(ary) and ary[i]>ary[i-1]:
            i=i+1
        sell=i-1
        tmp.append(ary[sell]-ary[buy])

    tmp.sort(reverse=True)
    for j in range(0,k):
        profit=profit+tmp[j]
    return profit

def main():

    ary=[5, 2, 4, 0, 1,0,3,2,7]
    k=2
    print(DailyCodingProblem408(ary,k))

if __name__=='__main__':
    main()