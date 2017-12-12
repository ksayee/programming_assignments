def non_recurring(ary):

    lst={}
    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys():
            lst[key]=lst.get(key)+1
        else:
            lst[key]=1

    for i in range(0,len(ary)):
        key=ary[i]
        if key in lst.keys() and lst.get(key)==1:
            return key

def main():
    ary=[4,8,4,7,8,5,2,7,3,2,1,1]

    print('First Non-recurring element is: ',non_recurring(ary))

if __name__=='__main__':
    main()
