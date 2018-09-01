# Given two unsorted arrays, find all pairs whose sum is x
# Given two unsorted arrays of distinct elements,
# the task is to find all pairs from both arrays whose sum is equal to x.

def PairSumTwoArray(a1,a2,k):

    dict={}

    for l in a1:
        if l not in dict.keys():
            dict[l]=1

    fnl_lst=[]
    for l in a2:
        diff=k-l
        if diff in dict.keys():
            tup=(diff,l)
            fnl_lst.append(tup)

    return fnl_lst

def main():

    a1=[ -1, -2, 4, -6, 5, 7]
    a2=[6, 3, 4, 0]
    k=8
    print(PairSumTwoArray(a1,a2,k))

    a1 = [1, 2, 4, 5, 7]
    a2 = [5, 6, 3, 4, 8]
    k = 9
    print(PairSumTwoArray(a1, a2, k))

if __name__=='__main__':
    main()