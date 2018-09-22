'''
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''


def LeetCode167(ary,k):

    dict={}

    fnl_lst=[]
    for i in range(0,len(ary)):
        key=ary[i]
        diff=k-key
        if diff!=key:

            if diff in dict.keys():
                tmp=[]
                for l in dict[diff]:
                    tmp.append(l+1)
                tmp.append(i+1)
                fnl_lst.append(tmp)
            elif key not in dict.keys():
                tmp=[]
                tmp.append(i)
                dict[key]=tmp
            else:
                dict[key].append(i)

    return fnl_lst

def main():

    ary=[2,7,11,15]
    k=9
    print(LeetCode167(ary,k))

    print(bin(2))

if __name__=='__main__':
    main()