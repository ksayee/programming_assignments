# Smallest greater elements in whole array
# An array is given of n length, and we need to calculate the next greater element for each element in given array.
# If next greater element is not available in given array then we need to fill ‘_’ at that index place.

def SmallestGreaterElementWholeArray(ary):

    lst=sorted(ary)

    fnl_lst=[]

    for i in range(0,len(ary)):

        key=ary[i]

        idx=lst.index(key)
        if idx==-1 or idx==len(lst)-1:
            fnl_lst.append('_')
        else:
            fnl_lst.append(str(lst[idx+1]))

    return fnl_lst

def main():

    ary=[6,3,9,8,10,2,1,15,7]
    print(SmallestGreaterElementWholeArray(ary))

    ary = [13,6,7,12]
    print(SmallestGreaterElementWholeArray(ary))

if __name__=='__main__':
    main()