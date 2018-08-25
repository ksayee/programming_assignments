# Non-overlapping sum of two sets
# Given two arrays A[] and B[] of size n. It is given that both array individually contain distinct elements.
# We need to find sum of all elements that are not common.

def SumNotCommonElements(lst1,lst2):

    dict={}

    for l in lst1:

        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1

    for l in lst2:

        if l in dict.keys():
            dict[l]=dict.get(l)+1
        else:
            dict[l]=1

    sum=0
    for key,val in dict.items():
        if val==1:
            sum=sum+key

    return sum

def main():
    
    lst1=[1, 5, 3, 8]
    lst2=[5, 4, 6, 7]
    print(SumNotCommonElements(lst1,lst2))

    lst1 = [1, 5, 3, 8]
    lst2 = [5, 1, 8, 3]
    print(SumNotCommonElements(lst1, lst2))

if __name__=='__main__':
    main()