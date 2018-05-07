'''
Given a String=['us','uk','in'] give all the combinations of string.
'''

import copy

def StringCombinations(lst,tmp_lst,idx,res_lst):

    for i in range(idx,len(lst)):
        tmp_lst.append(lst[i])
        cp_lst=copy.copy(tmp_lst)
        res_lst.append(cp_lst)
        StringCombinations(lst,copy.copy(tmp_lst),i+1,res_lst)
        tmp_lst=tmp_lst[0:-1]

    return res_lst

def main():

    lst=['us','uk','in']
    res_lst=[]
    print(sorted(StringCombinations(lst,[],0,res_lst),key=lambda x:len(x)))

    lst = ['us','uk','in','br']
    res_lst = []
    print(sorted(StringCombinations(lst, [], 0, res_lst),key=lambda x:len(x)))


if __name__=='__main__':
    main()
