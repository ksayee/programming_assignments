'''
341. Flatten Nested List Iterator
Given a nested list of integers, implement an iterator to flatten it.
Each element is either an integer, or a list -- whose elements may also be integers or other lists.
Example 1:
Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
'''

def flatten_list_recur(ary):

    output_lst=[]
    for l in ary:
        if isinstance(l,list):
            output_lst.extend(flatten_list_recur(l))
        else:
            output_lst.append(l)
    return output_lst

def LeetCode341(ary):

    lst=flatten_list_recur(ary)
    return lst

def main():

    ary=[[1,1],2,[1,1]]
    print(LeetCode341(ary))

    ary = [1,[4,[6]]]
    print(LeetCode341(ary))

    ary = [1,[4,[6,[8,7,[98,73],3]]],[36,21]]
    print(LeetCode341(ary))

if __name__=='__main__':
    main()