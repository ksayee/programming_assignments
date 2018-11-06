'''
Given an Input: Hashmap('a' -> 'b', 'b' -> 'c', 'x' -> 'y', 'd' -> 'b)
Output hashmap('c' - > set('a','b','c','d'), 'y' -> set('x','y')

Description:
a can be replaced by b,
b can be replaced by c,
Hence a can be replaced by c
x can be replaced by y
d can be replaced by b

a cluster id is that key which can't be replaced
'''

def Getlist_data(lst,tmp,rev_dict):

    if len(lst)==0:
        return

    for l in lst:
        tmp.append(l)
        if l in rev_dict.keys():
            Getlist_data(rev_dict[l],tmp,rev_dict)

def GetClusters(ary):

    dict={}

    for tup in ary:
        dict[tup[0]]=tup[1]

    rev_dict={}

    for key,val in dict.items():
        if val in rev_dict.keys():
            rev_dict[val].append(key)
        else:
            tmp=[]
            tmp.append(key)
            rev_dict[val]=tmp

    cl_lst=[]
    for key,val in rev_dict.items():
        if key not in dict.keys():
            cl_lst.append(key)

    fnl_lst={}
    for key in cl_lst:

        tmp=[]
        tmp.append(key)
        if key in rev_dict.keys():
            Getlist_data(rev_dict[key],tmp,rev_dict)

        fnl_lst[key]=sorted(set(tmp))
    return fnl_lst

def main():

    ary=[('a', 'b'),('b','c'),('x','y'),('d','b')]
    print(GetClusters(ary))

if __name__=='__main__':
    main()