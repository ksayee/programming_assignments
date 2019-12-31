'''
Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array,
find the max profit that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
Recommended: Please solve it on “PRACTICE ” first, before moving on to the solution.
Naive approach: A simple approach is to try buying the stocks and selling them on every single day when profitable and keep updating the maximum profit so far.
Below is the implementation of the above approach:
'''

def StockBuySellToMaximizeProfit(ary):

    buy=-1
    sell=-1
    i=1
    print('New Input')
    profit=0
    while i<len(ary):
        while i<len(ary) and ary[i]<ary[i-1]:
            i=i+1
        if i==len(ary):
            break
        buy=i-1
        while i<len(ary) and ary[i]>ary[i-1]:
            i=i+1
        sell=i-1
        print('Buy Stock on: ',buy, ' Day')
        print('Sell Stock on: ', sell, ' Day')
        profit=profit+ary[sell]-ary[buy]
    print('TotalP Profit: ', profit)

def main():

    ary=[7,1,5,3,6,4]
    StockBuySellToMaximizeProfit(ary)

    ary = [1,2,3,4,5]
    StockBuySellToMaximizeProfit(ary)

    ary = [7,6,4,3,1]
    StockBuySellToMaximizeProfit(ary)

    ary = [100, 180, 260, 310,40, 535, 695]
    StockBuySellToMaximizeProfit(ary)

if __name__=='__main__':
    main()