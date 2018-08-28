# Replace every element with the greatest element on right side
# Given an array of integers, replace every element with the next greatest element
# (greatest element on the right side) in the array.
# Since there is no element next to the last element, replace it with -1.
# For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.

def ReplaceWithGreatestElement(ary):

    max=0

    for i in range(len(ary)-1,-1,-1):

        if i==len(ary)-1:
            max=ary[i]
            ary[i]=-1
        else:
            if ary[i]>max:
                tmp=ary[i]
                ary[i]=max
                max=tmp
            else:
                ary[i]=max

    return ary

def main():
    
    ary=[16, 17, 4, 3, 5, 2]
    print(ReplaceWithGreatestElement(ary))

if __name__=='__main__':
    main()