'''
Find a triplet such that sum of two equals to third element
Given an array of integers you have to find three numbers such that sum of two elements equals the third element.
Examples:
Input : {5, 32, 1, 7, 10, 50, 19, 21, 2}
Output : 21, 2, 19
Input : {5, 32, 1, 7, 10, 50, 19, 21, 0}
Output : no such triplet exist
'''

def TripletSumTwoElementsEqualThirdElement(ary):
    ary.sort()
    output_lst=[]
    for i in range(len(ary)-1,-1,-1):
        left=0
        right=i-1
        while left < right:
            if ary[left]+ary[right]==ary[i]:
                output_lst.append((ary[left],ary[right],ary[i]))
                left=left+1
                right=right-1
            elif ary[left]+ary[right]<ary[i]:
                left=left+1
            else:
                right=right-1
    return output_lst

def main():

    ary=[5, 32, 1, 7, 10, 50, 19, 21, 2]
    print(TripletSumTwoElementsEqualThirdElement(ary))

    ary = [5, 32, 1, 7, 10, 50, 19, 21, 0]
    print(TripletSumTwoElementsEqualThirdElement(ary))

if __name__=='__main__':
    main()