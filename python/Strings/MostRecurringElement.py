def non_recurring(ary):

    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1
    max=0
    for key, val in lst.items():
        if val>max:
            max=key

    return max

def main():
    ary=[4,8,4,7,8,8,5,2,7,3,2,1,1]

    print('Most recurring element is: ',non_recurring(ary))

if __name__=='__main__':
    main()
