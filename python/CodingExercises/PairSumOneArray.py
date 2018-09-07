# Given an array A[] and a number x, check for pair in A[] with sum as x
# Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist two elements in S whose sum is exactly x.

def PairSumOneArray(ary,n):

    dict={}

    fnl_lst=[]
    for l in ary:
        num=n-l
        if num in dict.keys():
            tup=(l,num)
            fnl_lst.append(tup)
        else:
            dict[l]=1

    return fnl_lst

def main():
    
    ary=[1, 4, 45, 6, 10, -8]
    n=16
    print(PairSumOneArray(ary,16))

if __name__=='__main__':
    main()