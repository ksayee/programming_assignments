# Find missing elements of a range
# Given an array arr[0..n-1] of distinct elements and a range [low, high],
# find all numbers that are in range, but not in array. The missing elements should be printed in sorted order.

def MissingElementsRange(ary,low,high):

    fnl_lst=[]

    while low<=high:

        if low not in ary:
            fnl_lst.append(low)
        low=low+1

    return fnl_lst

def main():

    ary=[10, 12, 11, 15]
    low=10
    high=15
    print(MissingElementsRange(ary,low,high))

    ary = [1, 14, 11, 51, 15]
    low = 50
    high = 55
    print(MissingElementsRange(ary, low, high))

if __name__=='__main__':
    main()