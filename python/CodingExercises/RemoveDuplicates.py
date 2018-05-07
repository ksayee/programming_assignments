def removeduplicates(ary):

    lst=[]

    for i in range(0,len(ary)):
        key=ary[i]

        if key not in lst:
            lst.append(key)
    return lst

def removeduplicates_onelist(ary):

    l=len(ary)
    i=0
    while i<l:
        key=ary[i]

        if key in ary[i+1:]:
            del ary[i]
            l=l-1
        else:
            i=i+1
    return ary

def main():

    ary = [1, 1, 1, 2, 2, 3, 5, 5, 7, 7, 7, 8, 9, 10, 34, 34, 56, 56, 56]
    print(removeduplicates(ary))
    print(removeduplicates_onelist(ary))

if __name__=='__main__':
    main()