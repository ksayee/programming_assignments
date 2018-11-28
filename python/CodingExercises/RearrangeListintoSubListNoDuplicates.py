'''
Given a list of strings, rearrange the strings into a list of lists of strings where each inner list contains no duplicates. Return the list of lists.

For example:

["a", "b", "c", "a", "a", "b"] -> [ ["a", "b", "c"], ["a", "b"], ["a"] ]

This is not a unique solution; [ ["a", "b"], ["a", "b"], ["a", "c"] ] would also be a valid output. You only need to return one valid output.

Order does not matter in any way for either the input or the output.

Your solution should minimize the number of inner lists.

For example:

[ ["a"], ["a"], ["b"] ] would not be a correct solution for ["a", "a", "b"].

The correct solution would be [ ["a", "b"], ["a"] ]
'''

def UpdatePreviousList(l,fnl_lst):

    flg=False

    for lst in fnl_lst:

        if l not in lst:
            lst.append(l)
            flg=True
            break
    return flg

def RearrangeListintoSubListNoDuplictes(ary):

    tmp=[]
    fnl_lst=[]
    for l in ary:

        if l not in tmp:
            tmp.append(l)
        else:
            flg=UpdatePreviousList(l,fnl_lst)
            if flg==False:
                fnl_lst.append(tmp.copy())
                tmp=[]
                tmp.append(l)
    if len(tmp)>0:
        fnl_lst.append(tmp.copy())

    return fnl_lst

def main():

    ary=["a", "b", "c", "a", "a", "b"]
    print(RearrangeListintoSubListNoDuplictes(ary))

    ary = ["a", "a", "a", "b"]
    print(RearrangeListintoSubListNoDuplictes(ary))

    ary = ["a", "b", "c", "d", "a", "b"]
    print(RearrangeListintoSubListNoDuplictes(ary))

    ary = ["a", "b", "b", "b", "a", "a"]
    print(RearrangeListintoSubListNoDuplictes(ary))

if __name__=='__main__':
    main()