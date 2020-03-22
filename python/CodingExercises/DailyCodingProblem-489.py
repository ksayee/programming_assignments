'''
This problem was asked by Google.
Given an array of elements, return the length of the longest subarray where all its elements are distinct.
For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

def DailyCodingProblem489(ary):
    dict={}
    output_lst=[]
    idx=0
    for i in range(0,len(ary)):
        key=ary[i]
        if key not in dict.keys():
            dict[key]=i
        else:
            output_lst.append(ary[idx:i])
            num=dict[key]
            while idx<=num:
                del dict[ary[idx]]
                idx=idx+1
            dict[key]=i
    output_lst.append(ary[idx:])
    return sorted(output_lst,key=lambda x:len(x),reverse=True)[0]

def main():

    ary=[5, 1, 3, 5, 2, 3, 4, 1]
    print(DailyCodingProblem489(ary))

if __name__=='__main__':
    main()