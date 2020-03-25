'''
Given a list of sorted numbers find the number of 2 numbers whose sum is less that the target value
'''

def SortedArraryTwoNumberSumLessThanTarget(ary,target):

    left=0
    right=len(ary)-1
    output_lst=[]
    while left<right:
        sum=ary[left]+ary[right]
        if sum>=target:
            right=right-1
        else:
            tup=(ary[left],ary[right])
            output_lst.append(tup)
            k=right-1
            while k>left:
                tup = (ary[left], ary[k])
                output_lst.append(tup)
                k=k-1
            left=left+1
    return output_lst


def main():
    
    ary=[5,6,8,10,12,16,18,20,24,29]
    target=30
    print(SortedArraryTwoNumberSumLessThanTarget(ary,target))

if __name__=='__main__':
    main()