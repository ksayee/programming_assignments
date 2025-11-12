'''
Given an array of n positive integers, find a contiguous subarray (containing more than one number) with the largest min + max.

# - The array contains at least 2 elements.
# - All the numbers are positive integers.
'''

'''
Solution:

First find all the subarrays which are more than 2 elements and then solve the problem.
'''

def subarray_recur(start,end,tmp_lst,input_ary,subarray_lst):

    if end == len(input_ary):
        return
    else:
        tmp_lst = input_ary[start:end+1]
        if len(tmp_lst)>=2:
            if tmp_lst not in subarray_lst:
                subarray_lst.append(tmp_lst.copy())
        subarray_recur(start, end+1, tmp_lst, input_ary, subarray_lst)
        subarray_recur(start+1, start+2, tmp_lst, input_ary, subarray_lst)

def solution(input_ary):

    subarray_lst = []

    start =0
    end =1
    tmp_lst = []

    subarray_recur(start,end,tmp_lst,input_ary,subarray_lst)

    print("All Subarrays:", subarray_lst)

    output_dict={}

    for lst in subarray_lst:
        current_sum = min(lst) + max(lst)
        if current_sum in output_dict.keys():
            output_dict[current_sum].append(lst.copy())
        else:
            output_dict[current_sum] = []
            output_dict[current_sum].append(lst.copy())

    print("Output Dict:", output_dict)

    return sorted(output_dict.items(),key = lambda x:x[0],reverse=True)[0]

def main():

    input_ary=[2, 1, 5,4, 3, 4]
    print(solution(input_ary))

if __name__ == '__main__':
    main()