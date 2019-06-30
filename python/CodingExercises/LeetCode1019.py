'''
1019. Next Greater Node In Linked List
We are given a linked list with head as the first node.
Let's number the nodes in the list: node_1, node_2, node_3, ... etc.
Each node may have a next larger value: for node_i,
next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.
Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).
Note that in the example inputs (not outputs) below, arrays such as [2,1,5]
 represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.
'''

def LeetCode1019(ary):

    stk=[]

    fnl_lst=[-1]*len(ary)
    for i in range(0,len(ary)):
        if len(stk)==0:
            tup=(ary[i],i)
            stk.append(tup)
        else:
            if ary[i]>stk[-1][0]:
                while ary[i]>stk[-1][0]:
                    idx=stk[-1][1]
                    fnl_lst[idx]=ary[i]
                    stk.pop()
                    if len(stk)==0:
                        break
            tup = (ary[i], i)
            stk.append(tup)
    return fnl_lst

def main():

    ary = [5,3,2,10,6,8,1,4,12,7,4]
    print(LeetCode1019(ary))

    ary=[2,1,5]
    print(LeetCode1019(ary))

    ary = [2,7,4,3,5]
    print(LeetCode1019(ary))

    ary = [1,7,5,1,9,2,5,1]
    print(LeetCode1019(ary))

if __name__=='__main__':
    main()