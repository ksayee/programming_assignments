# Check if a given array contains duplicate elements within k distance from each other
# Given an unsorted array that may contain duplicates. Also given a number k which is smaller than size of array.
# Write a function that returns true if array contains duplicates within k distance.

def DuplicateElementsKDistance(ary,k):

    dict={}

    for i in range(0,len(ary)):

        key=ary[i]

        if key in dict.keys():
            dict[key].append(i)
        else:
            tmp=[]
            tmp.append(i)
            dict[key]=tmp

    fnl_lst=[]
    for key,val in dict.items():

        for j in range(1,len(val)):

            if val[j]-val[j-1]==k:
                tup=(val[j],val[j-1])
                tmp=[]
                tmp.append(key)
                tmp.append(tup)
                fnl_lst.append(tmp)

    return fnl_lst

def main():

    ary=[1, 2, 3, 4, 1, 2, 3, 4]
    k=4
    print(DuplicateElementsKDistance(ary,k))

    ary = [1, 2, 3, 1, 4, 5]
    k = 3
    print(DuplicateElementsKDistance(ary,k))

    ary = [1, 2, 3, 4, 5]
    k = 3
    print(DuplicateElementsKDistance(ary,k))

    ary = [1, 2, 3, 4, 4]
    k = 1
    print(DuplicateElementsKDistance(ary,k))

if __name__=='__main__':
    main()