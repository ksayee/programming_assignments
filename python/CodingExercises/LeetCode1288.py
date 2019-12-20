'''
1288. Remove Covered Intervals
Medium
Given a list of intervals, remove all intervals that are covered by another interval in the list.
Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.
Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
'''

def LeetCode1288(ary):

    sort_list=sorted(ary,key=lambda x:x[0])
    output_list=[]
    output_list.append(sort_list[0])
    k=0
    for i in range(1,len(sort_list)):
        tmp_list=sort_list[i]
        if tmp_list[0]>=output_list[k][0] and tmp_list[1]<=output_list[k][1]:
            pass
        else:
            output_list.append(tmp_list.copy())
            k=k+1
    return output_list
        
def main():

    ary=[[1,4],[3,6],[2,8]]
    print(LeetCode1288(ary))

if __name__=='__main__':
    main()