# Print n smallest elements from given array in their original order
# We are given an array of m-elements,
# we need to find n smallest elements from the array but they must be in the same order as they are in given array.

def nSmallestElementsArrayOrignalOrder(ary,k):

    lst=sorted(ary)

    sml_lst=lst[:k]

    fnl_lst=[]
    for i in range(0,len(ary)):

        key=ary[i]

        if key in sml_lst:
            fnl_lst.append(key)
        if len(fnl_lst)==len(sml_lst):
            break

    return fnl_lst

def main():

    ary=[4, 2, 6, 1, 5]
    k=3
    print(nSmallestElementsArrayOrignalOrder(ary,k))

    ary = [4, 12, 16, 21, 25]
    k = 3
    print(nSmallestElementsArrayOrignalOrder(ary, k))

if __name__=='__main__':
    main()