'''
'''

def flattenlist(lst):

    fnl_lst=[]
    fnl_lst=flattenlist_recur(lst)

    return fnl_lst

def flattenlist_recur(lst):

    fnl_lst=[]

    for l in lst:
        if isinstance(l,list):
            fnl_lst.extend(flattenlist_recur(l))
        else:
            fnl_lst.append(l)
    return fnl_lst


def main():
    
    lst=[1,[2,3,4,5],6,7,[8,9,[10,11]]]
    print(flattenlist(lst))

if __name__=='__main__':
    main()