# Pairs of Positive Negative values in an array
# Given an array of distinct integers,
# print all the pairs having positive value and negative value of a number that exists in the array.
# We need to print pairs in order of their occurrences. A pair whose any element appears first should be printed first.

def PositiveNegativePairs(ary):

    dict={}

    for l in ary:

        key=abs(l)
        if key in dict.keys():
            dict[key]=dict.get(key)+1
        else:
            dict[key]=1

    fnl_lst=[]
    for key,val in dict.items():
        if val==2:
            tup=(key,(-1)*key)
            fnl_lst.append(tup)

    return fnl_lst

def main():
    
    ary=[1, -3, 2, 3, 6, -1]
    print(PositiveNegativePairs(ary))

    ary = [4, 8, 9, -4, 1, -1, -8, -9]
    print(PositiveNegativePairs(ary))

if __name__=='__main__':
    main()