def non_recurring(ary):

    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1
    max_val=0
    max_key=0
    for key, val in lst.items():
        if val>max_val:
            max_key=key
            max_val=val

    return max_key

def main():
    ary=[4,8,4,7,8,8,5,2,7,7,7,7,3,2,1,1]

    print('Most recurring element is: ',non_recurring(ary))

if __name__=='__main__':
    main()
