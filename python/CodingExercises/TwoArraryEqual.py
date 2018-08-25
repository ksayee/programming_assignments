# Check if two arrays are equal or not
# Given two given arrays of equal length, the task is to find if given arrays are equal or not.
# Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of elements may be different though.

def TwoArrayEqual(lst1,lst2):

    if len(lst1)!=len(lst2):
        return False
    else:

        tmp=[0]*10

        for l in lst1:
            tmp[l]=tmp[l]+1
        for l in lst2:
            tmp[l]=tmp[l]-1

        for i in range(0,len(tmp)):
            if tmp[i]!=0:
                return False
        return True

def main():

    lst1=[1, 2, 5, 4, 0]
    lst2=[2, 4, 5, 0, 1]
    print(TwoArrayEqual(lst1,lst2))

    lst1 = [1, 2, 5, 4, 0, 2, 1]
    lst2 = [2, 4, 5, 0, 1, 1, 2]
    print(TwoArrayEqual(lst1, lst2))

    lst1 = [1, 7, 1]
    lst2 = [7, 7, 1]
    print(TwoArrayEqual(lst1, lst2))

if __name__=='__main__':
    main()