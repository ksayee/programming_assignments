'''
228. Summary Ranges
Medium
Given a sorted integer array without duplicates, return the summary of its ranges.
Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

def LeetCode228(ary):

    fnl_lst=[]
    tmp=[]
    for i in range(0,len(ary)):
        key=ary[i]
        if len(tmp)==0:
            tmp.append(key)
        else:
            if key-tmp[-1]==1:
                tmp.append(key)
            else:
                if len(tmp)==1:
                    tup=[tmp[0]]
                else:
                    tup=[tmp[0],tmp[-1]]
                fnl_lst.append(tup.copy())
                tmp=[]
                tmp.append(key)
    if len(tmp)>0:
        if len(tmp) == 1:
            tup = [tmp[0]]
        else:
            tup = [tmp[0], tmp[-1]]
        fnl_lst.append(tup.copy())
        tmp = []
    return fnl_lst

def main():

    ary=[0,1,2,4,5,7]
    print(LeetCode228(ary))

    ary = [0,2,3,4,6,8,9]
    print(LeetCode228(ary))

if __name__=='__main__':
    main()