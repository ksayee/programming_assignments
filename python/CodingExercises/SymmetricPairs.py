# Given an array of pairs, find all symmetric pairs in it
# Two pairs (a, b) and (c, d) are said to be symmetric if c is equal to b and a is equal to d.
# For example (10, 20) and (20, 10) are symmetric. Given an array of pairs find all symmetric pairs in it.

def SymmetricPairs(ary):

    dict={}

    fnl_lst=[]
    for l in ary:

        key=l[0]
        val=l[1]

        if val in dict.keys():
            if dict[val]==key:
                tmp=[]
                tmp.append(l)
                tmp.append((val,key))
                fnl_lst.append(tmp)
        else:
            dict[key]=val

    return fnl_lst

def main():

    ary=[(11, 20), (30, 40), (5, 10), (40, 30), (10, 5)]
    print(SymmetricPairs(ary))

if __name__=='__main__':
    main()