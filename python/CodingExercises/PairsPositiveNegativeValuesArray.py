'''
Pairs of Positive Negative values in an array
Given an array of distinct integers,
print all the pairs having positive value and negative value of a number that exists in the array.
We need to print pairs in order of their occurrences.
A pair whose any element appears first should be printed first.

Examples:

Input  :  arr[] = { 1, -3, 2, 3, 6, -1 }
Output : -1 1 -3 3

Input  :  arr[] = { 4, 8, 9, -4, 1, -1, -8, -9 }
Output : -1 1 -4 4 -8 8 -9 9
'''

def PairsPositiveNegativeValuesArray(ary):

    stk=[]
    dict={}
    fnl_lst=[]

    for l in ary:
        stk.append(l)
        if l not in dict.keys():
            if (-1)*l in dict.keys():
                dict[(-1)*l]=2
            else:
                dict[l]=1

    for l in stk:
        if (l in dict.keys() or (-1)*l in dict.keys()):
            try:
                if dict[l]==2:
                    if l<0:
                        fnl_lst.append(l)
                        fnl_lst.append((-1)*l)
                    else:
                        fnl_lst.append((-1) * l)
                        fnl_lst.append(l)
                    dict[l]=0
            except:
                if dict[(-1)*l]==2:
                    if l<0:
                        fnl_lst.append(l)
                        fnl_lst.append((-1)*l)
                    else:
                        fnl_lst.append((-1) * l)
                        fnl_lst.append(l)
                    dict[(-1) * l] = 0
    return fnl_lst

def main():

    ary=[1, -3, 2, 3, 6, -1]
    print(PairsPositiveNegativeValuesArray(ary))

    ary = [4, 8, 9, -4, 1, -1, -8, -9]
    print(PairsPositiveNegativeValuesArray(ary))


if __name__=='__main__':
    main()