'''
Split an array into two equal Sum subarrays
Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

Examples :

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 }
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
'''

def SplitArraryEqualHalfSum(ary):

    leftSum=0
    rightSum=0

    for key in ary:
        leftSum=leftSum+key

    for i in range(len(ary)-1,-1,-1):
        rightSum=rightSum+ary[i]
        leftSum=leftSum-ary[i]

        if rightSum==leftSum:
            break

    if i==0:
        return -1

    output_lst=[]
    tmp=[]
    for j in range(0,len(ary)):
        if j==i:
            output_lst.append(tmp.copy())
            tmp=[]
        tmp.append(ary[j])
    output_lst.append(tmp.copy())
    return output_lst

def main():

    ary=[1 , 2 , 3 , 4 , 5 , 5 ]
    print(SplitArraryEqualHalfSum(ary))

    ary = [4, 1, 2, 3 ]
    print(SplitArraryEqualHalfSum(ary))

    ary = [4, 3, 2, 1]
    print(SplitArraryEqualHalfSum(ary))

if __name__=='__main__':
    main()