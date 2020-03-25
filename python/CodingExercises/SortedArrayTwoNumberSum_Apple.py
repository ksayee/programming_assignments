'''
Given a list of sorted numbers find the number of 2 numbers which add up to the given sum
'''

def SortedArraryTwoNumberSum(ary,target):

    left=0
    right=len(ary)-1
    output_lst=[]
    while left<right:
        sum=ary[left]+ary[right]
        if sum==target:
            tup=(ary[left],ary[right])
            output_lst.append(tup)
            left=left+1
            right=right-1
        elif sum>target:
            right=right-1
        else:
            left=left+1
    return output_lst


def main():
    
    ary=[5,6,8,10,12,16,18,20,24,29]
    target=30
    print(SortedArraryTwoNumberSum(ary,target))

if __name__=='__main__':
    main()