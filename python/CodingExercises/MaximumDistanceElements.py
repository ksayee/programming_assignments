# Maximum distance between two occurrences of same element in array
# Given an array with repeated elements, the task is to find the maximum distance two occurrences of an element.

def MaximumDeleteElements(ary):

    dict={}

    for i in range(0,len(ary)):

        key=ary[i]

        if key in dict.keys():
            dict[key].append(i)
        else:
            tmp=[]
            tmp.append(i)
            dict[key]=tmp

    fnl_lst=[]
    for key,val in dict.items():

        if len(val)>1:
            num=val[len(val)-1]-val[0]
            tup=(key,num)
            fnl_lst.append(tup)

    return fnl_lst

def main():

    ary=[3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
    print(MaximumDeleteElements(ary))

if __name__=='__main__':
    main()