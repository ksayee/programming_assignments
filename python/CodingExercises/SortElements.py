# Sort elements by frequency | Set 4 (Efficient approach using hash)
# Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.

import collections
def SortElements(ary):

    dict=collections.Counter(ary)

    sort_dict=sorted(dict.items(),key=lambda x:x[1],reverse=True)

    idx_dict={}

    for key,val in sort_dict:
        idx=ary.index(key)

        if val in idx_dict.keys():
            idx_dict[val].append(idx)
        else:
            tmp=[]
            tmp.append(idx)
            idx_dict[val]=tmp

    sort_tmp=sorted(idx_dict.items(),key=lambda x:x[0],reverse=True)
    
    fnl_lst=[]
    for key,val in sort_tmp:
        for k in val:
            itm=ary[k]
            n=0
            while n<key:
                fnl_lst.append(itm)
                n=n+1

    return fnl_lst


def main():
    
    ary=[2, 5, 2, 8, 5, 6, 8, 8]
    print(SortElements(ary))

    ary = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    print(SortElements(ary))

if __name__=='__main__':
    main()