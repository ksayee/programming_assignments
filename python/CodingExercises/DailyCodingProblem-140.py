'''
This problem was asked by Facebook.
Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.
For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.
Follow-up: Can you do this in linear time and constant space?
'''

def DailyCodingProblem140(ary):

    fnl_lst=[]

    for i in range(0,len(ary)):
        key=ary[i]
        if key not in ary[:i] and key not in ary[i+1:]:
            fnl_lst.append(key)

    return fnl_lst

def main():

    ary=[2, 4, 6, 8, 10, 2, 6, 10]
    print(DailyCodingProblem140(ary))

if __name__=='__main__':
    main()