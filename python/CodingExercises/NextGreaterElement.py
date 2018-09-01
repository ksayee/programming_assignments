# Next Greater Element
# Given an array, print the Next Greater Element (NGE) for every element.
# The Next greater Element for an element x is the first greater element on the right side of x in array.
# Elements for which no greater element exist, consider next greater element as -1.
# Examples:
# a) For any array, rightmost element always has next greater element as -1.
# b) For an array which is sorted in decreasing order, all elements have next greater element as -1.
# c) For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

def NextGreaterElement(ary):

    lst=[]

    fnl_lst=[0]*len(ary)
    tup=(ary[0],0)
    lst.append(tup)

    for i in range(1,len(ary)):

        key=ary[i]
        if len(lst)>0:
            tup=lst.pop()

        tmp=tup[0]
        idx=tup[1]

        while key>tmp:
            fnl_lst[idx]=key
            if len(lst) > 0:
                tup=lst.pop()
                tmp = tup[0]
                idx = tup[1]
            else:
                break

        if tmp>key:
            lst.append(tup)

        lst.append((key,i))

    while len(lst)!=0:
        if len(lst) > 0:
            tup=lst.pop()
            fnl_lst[tup[1]]=-1

    return fnl_lst

def main():

    ary=[4, 5, 2, 25]
    print(NextGreaterElement(ary))

    ary = [13, 7, 6, 12]
    print(NextGreaterElement(ary))

    ary = [11, 13, 21, 3]
    print(NextGreaterElement(ary))

if __name__=='__main__':
    main()