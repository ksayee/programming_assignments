'''
1380. Lucky Numbers in a Matrix
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
'''

def LeetCode1380(ary):

    output=[]
    flg=False
    for i in range(0,len(ary)):
        lst=ary[i]
        while True:
            min_num=min(lst)
            idx=lst.index(min_num)
            tmp=[]
            for j in range(0,len(ary)):
                tmp.append(ary[j][idx])
            max_num=max(tmp)
            if max_num==min_num:
                output.append(max_num)
                flg=True
            break
        if flg==True:
            break
    return output

def main():

    ary=[[3,7,8],[9,11,13],[15,16,17]]
    print(LeetCode1380(ary))

    ary = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    print(LeetCode1380(ary))

    ary = [[7,8],[1,2]]
    print(LeetCode1380(ary))

if __name__=='__main__':
    main()