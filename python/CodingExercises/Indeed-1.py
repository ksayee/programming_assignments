'''
        14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

parentChildPairs1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]
In the above graph, the output should container 2 lists, one which does not have any parent and another which has one parent.
'''

def Indeed(parentChildPairs):

    dict={}
    parents=[]
    childs=[]

    for tup in parentChildPairs:
        parent=tup[0]
        child=tup[1]
        if child in dict.keys():
            dict[child].append(parent)
        else:
            dict[child]=[]
            dict[child].append(parent)
        if parent not in parents:
            parents.append(parent)
        if child not in childs:
            childs.append(child)

    fnl_lst=[]
    tmp=[]
    for key,val in dict.items():
        if len(val)==1:
            tmp.append(key)
    fnl_lst.append(sorted(tmp.copy()))

    tmp=[]
    for parent in parents:
        if parent not in childs:
            tmp.append(parent)
    fnl_lst.append(sorted(tmp.copy()))

    return sorted(fnl_lst)

def main():

    parentChildPairs = [
        (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
        (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
    ]
    print(Indeed(parentChildPairs))

if __name__=='__main__':
    main()