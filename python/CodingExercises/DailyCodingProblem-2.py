'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def DailyCodingProblem2(ary):

    result=1

    for i in range(0,len(ary)):
        result=result*ary[i]

    fnl_lst=[]

    for i in range(0,len(ary)):
        fnl_lst.append(int(result/ary[i]))

    return fnl_lst

def DailyCodingProblem2_alternate(ary):

    left=[1]*len(ary)
    right=[1]*len(ary)

    for i in range(1,len(ary)):
        left[i]=left[i-1]*ary[i-1]

    for i in range(len(ary)-2,-1,-1):
        right[i]=right[i+1]*ary[i+1]

    fnl_lst=[]

    for i in range(0,len(ary)):
        fnl_lst.append(left[i]*right[i])

    return fnl_lst

def main():

    ary=[1, 2, 3, 4, 5]
    print(DailyCodingProblem2(ary))
    print(DailyCodingProblem2_alternate(ary))

    ary = [10, 3, 5, 6, 2]
    print(DailyCodingProblem2(ary))
    print(DailyCodingProblem2_alternate(ary))

    ary = [3, 2, 1]
    print(DailyCodingProblem2(ary))
    print(DailyCodingProblem2_alternate(ary))

if __name__=='__main__':
    main()